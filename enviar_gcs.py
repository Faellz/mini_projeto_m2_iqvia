# envio do arquivo bruto para Cloud Storage (bronze)

from google.cloud import storage
import config

def upload_to_bucket():

    client = storage.Client(project=config.PROJECT_ID)

    bucket = client.bucket(config.BUCKET_NAME)

    blob = bucket.blob("bronze/MS_12_2022_sample.xlsx")
    blob.upload_from_filename(config.LOCAL_FILE)

    print("Upload concluído!\n")

if __name__ == "__main__":
    upload_to_bucket()