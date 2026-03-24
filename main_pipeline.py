# executa o pipeline completo

from enviar_gcs import upload_to_bucket
from transform import transform_data
from load_bigquery import load_staging
from scd import run_scd

def run_pipeline():

    print("Iniciando pipeline...\n")

    upload_to_bucket()

    df = transform_data()
    df.to_csv("staging_produto.csv", index=False)

    load_staging()

    run_scd()

    print("Pipeline finalizado com sucesso!\n")

if __name__ == "__main__":
    run_pipeline()