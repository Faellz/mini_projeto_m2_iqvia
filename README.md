# mini_projeto_m2_iqvia
Mini Projeto ETL com SCD Tipo 2 (IQVIA)

Visão Geral
Este projeto implementa um pipeline de dados completo no padrão ETL (Extract, Transform, Load) utilizando Python e Google Cloud, com foco em controle de histórico de dados através de SCD Tipo 2 (Slowly Changing Dimension).
O objetivo é simular um cenário real do setor farmacêutico, onde alterações em produtos (como preço) precisam ser rastreadas ao longo do tempo.


Arquitetura
O pipeline segue a arquitetura em camadas:

Excel (dados brutos)
        ↓
Cloud Storage (Landing / Bronze)
        ↓
BigQuery (Silver - staging)
        ↓
BigQuery (Gold - dimensão histórica com SCD Tipo 2)

Tecnologias Utilizadas
Python
Google Cloud Storage (GCS)
BigQuery
Pandas
Google Cloud SDK (gcloud)

Como Executar
1. Autenticação
gcloud auth application-default login
2. Rodar pipeline completo
python main_pipeline.py

Teste do SCD Tipo 2
1. Execute o pipeline
2. Altere um valor no Excel
3. Execute novamente
