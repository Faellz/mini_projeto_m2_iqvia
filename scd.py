from google.cloud import bigquery
import config

def run_scd():

    client = bigquery.Client(project=config.PROJECT_ID)

    update_query = f"""
    UPDATE `{config.PROJECT_ID}.{config.DATASET_GOLD}.{config.TABLE_DIM}` T
    SET 
      flag_ativo = FALSE,
      data_fim_validade = CURRENT_DATE()
    WHERE flag_ativo = TRUE
    AND EXISTS (
        SELECT 1
        FROM `{config.PROJECT_ID}.{config.DATASET_SILVER}.{config.TABLE_STAGING}` S
        WHERE T.id_produto_original = S.id_produto_original
        AND T.valor_produto != S.valor_produto
    )
    """

    insert_query = f"""
    INSERT INTO `{config.PROJECT_ID}.{config.DATASET_GOLD}.{config.TABLE_DIM}`
    (
      sk_produto,
      id_produto_original,
      valor_produto,
      data_inicio_validade,
      data_fim_validade,
      flag_ativo
    )
    SELECT
      GENERATE_UUID(),
      S.id_produto_original,
      S.valor_produto,
      CURRENT_DATE(),
      CAST(NULL AS DATE),
      TRUE
    FROM `{config.PROJECT_ID}.{config.DATASET_SILVER}.{config.TABLE_STAGING}` S
    WHERE NOT EXISTS (
      SELECT 1
      FROM `{config.PROJECT_ID}.{config.DATASET_GOLD}.{config.TABLE_DIM}` T
      WHERE T.id_produto_original = S.id_produto_original
        AND T.flag_ativo = TRUE
    )
    """

    client.query(update_query).result()
    client.query(insert_query).result()

    print("SCD Tipo 2 executado com sucesso!")


if __name__ == "__main__":
    run_scd()