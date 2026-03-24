# limpeza e padronização usando Pandas (silver)

import pandas as pd
import config

def transform_data():

    df = pd.read_excel(config.LOCAL_FILE)

    df = df.rename(columns={
        "EAN": "id_produto_original",
        "Tipo Informacao SO Bandeira PRECO POPULAR Unidade": "valor_produto"
    })

    df = df[["id_produto_original", "valor_produto"]]

    df = df.dropna()

    df["id_produto_original"] = df["id_produto_original"].astype(str)
    
    df["valor_produto"] = df["valor_produto"].astype(float)

    df = df.drop_duplicates()
    
    df = df.groupby("id_produto_original", as_index=False).agg({
    "valor_produto": "max"
    })

    return df


if __name__ == "__main__":

    df = transform_data()
    df.to_csv("staging_produto.csv", index=False)

    print("Transformação concluída!\n")