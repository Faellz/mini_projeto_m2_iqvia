# Mini Projeto ETL com SCD Tipo 2 (IQVIA)

## Visão Geral

Este projeto implementa um pipeline de dados completo no padrão **ETL (Extract, Transform, Load)** utilizando Python e Google Cloud, com foco em **controle de histórico de dados através de SCD Tipo 2 (Slowly Changing Dimension)**.

O objetivo é simular um cenário real do setor farmacêutico, onde alterações em produtos (como preço) precisam ser rastreadas ao longo do tempo.

---

## Arquitetura

O pipeline segue a arquitetura em camadas:

```text
Excel (dados brutos)
        ↓
Cloud Storage (Landing / Bronze)
        ↓
BigQuery (Silver - staging)
        ↓
BigQuery (Gold - dimensão histórica com SCD Tipo 2)
```

---

## Tecnologias Utilizadas

* Python
* Google Cloud Storage (GCS)
* BigQuery
* Pandas
* Google Cloud SDK (gcloud)

---

## Como Executar

### 1. Autenticação

```bash
gcloud auth application-default login
```

---

### 2. Rodar pipeline completo

```bash
python main_pipeline.py
```

---

## Teste do SCD Tipo 2

1. Execute o pipeline
2. Altere um valor no Excel
3. Execute novamente

### Resultado esperado

| id_produto_original | valor_produto | flag_ativo |
| ------------------- | ------------- | ---------- |
| 42110200            | 99            | FALSE      |
| 42110200            | 120           | TRUE       |

---

## Conceitos Aplicados

* ETL moderno
* Data Lake vs Data Warehouse
* Arquitetura Bronze / Silver / Gold
* Slowly Changing Dimension (SCD Tipo 2)
* Idempotência

---

## Observações

* O pipeline é **idempotente** (não gera duplicidade ao rodar múltiplas vezes)
* A tabela Gold mantém **histórico completo de alterações**
* A camada Silver garante **1 registro por chave natural**

---

## Conclusão

Este projeto demonstra a construção de um pipeline de dados robusto e realista, aplicando boas práticas de engenharia de dados para garantir:

✔ rastreabilidade
✔ consistência
✔ histórico de mudanças
✔ escalabilidade

---

Desenvolvido como parte do Mini Projeto M2 - Engenharia de Dados.

