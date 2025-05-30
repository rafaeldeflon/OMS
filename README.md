## OMS

#### Resumo:

- Projeto de ciência de dados com foco na análise e modelagem estatística para cálculo da taxa de contaminação de indivíduos

#### Pastas:

- notebooks: pasta contendo os notebooks construídos no projeto

- aux_files: pasta contendo os arquivos auxiliares e bases

#### Descrição do problema
Você é um funcionário da OMS que deve avaliar os níveis de contaminação de um vírus em um determinado país. As pessoas dentro de uma sociedade podem estar conectadas de alguma maneira (familia, amizade ou trabalho) e cada pessoa possui um conjunto de atributos. Este vírus afeta esta sociedade como descrito a seguir:

- a taxa de contaminação varia de pessoa para pessoa;

- a taxa de contaminação de uma pessoa A para B é diferente de B para A e depende das características de ambas as pessoas (A e B);

- a contaminação só passa através de indivíduos conectados;

- não existe cura para essa doença;

#### O desafio

Foram coletados os dados de contaminação (ou seja, as taxas de contaminação) para metade desta sociedade. Neste problema, você deverá estimar a taxa para o restante dessa sociedade e decidir políticas de saúde com base nos resultados obtidos.
Observação: Para determinar as taxas de contaminação, devem ser levados em consideração tanto as características dos infectados quanto dos infectantes.

#### Detalhes da base de dados

Para o desenvolvimento e resolução do problema considere os dois arquivos CSV:
> individuos_espec.csv - contém características de cada indivíduo

- name: Id dos indivíduos

- idade: idade dos indivíduos

- estado_civil: Estado civil dos indivíduos

- qt_filhos: quantidade de filhos dos indivíduos

- estuda: caso estudem

- trabalha: caso trabalhem

- pratica_esportes: caso pratiquem esportes

- transporte_mais_utilizado: qual o transporte mais utilizado

- IMC: valor do índice de massa corporal dos indivíduos

> conexoes_espec.csv - lista das conexões e algumas características das mesmas

- V1: id do individuo (relação entre os indivíduos)

- V2: id do individuo (relação entre os indivíduos)

- grau: familia, amigos, trabalho

- proximidade: mora_junto, visita_frequente, visita_casual, visita_rara

- prob_V1_V2: taxa de contaminação de V1 (doente) para V2 (saudável)
