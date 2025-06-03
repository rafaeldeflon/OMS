# Imports
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Carregando a pipeline do modelo treinado
model = joblib.load('modelo/xgb_pipeline.pkl')

# Lista de features
FEATURES = ['grau', 'proximidade', 
            
            'idade_V1', 'estado_civil_V1', 'qt_filhos_V1', 'estuda_V1', 'trabalha_V1', 
            'pratica_esportes_V1', 'transporte_mais_utilizado_V1', 'IMC_V1', 

            'idade_V2', 'estado_civil_V2', 'qt_filhos_V2', 'estuda_V2', 'trabalha_V2', 
            'pratica_esportes_V2', 'transporte_mais_utilizado_V2', 'IMC_V2']



# Configurando o Flask para rodar o modelo
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

# Erros de formato    
    if not data or 'data' not in data:
        return jsonify({"error": "JSON deve conter o campo 'data'"}), 400
    
    features = data['data']
    
    if len(features) != len(FEATURES):
        return jsonify({"error": f"Esperado {len(FEATURES)} features, recebido {len(features)}"}), 400

    try:
        df = pd.DataFrame([features], columns=FEATURES)
        prediction = model.predict(df)[0]
        return jsonify({"prediction": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)