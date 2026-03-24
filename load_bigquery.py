# carga para BigQuery (silver)

from google.cloud import bigquery
import pandas as pd
import config

def load_staging():

    client = bigquery.Client()

    df = pd.read_csv("staging_produto.csv", dtype={"id_produto_original": str})

    table_id = f"{config.PROJECT_ID}.{config.DATASET_SILVER}.{config.TABLE_STAGING}"

    job = client.load_table_from_dataframe(df, table_id)

    job.result()

    print("Dados carregados na tabela staging!\n")


if __name__ == "__main__":
    load_staging()