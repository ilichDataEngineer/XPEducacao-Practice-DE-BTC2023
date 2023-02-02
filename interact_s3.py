import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-ib-igti-edc",
                        "data/NpsResponses-rId-c787f79a-1076-4588-b453-f4cec9b9adf5.csv",
                        "data/nps.csv")

df = pd.read_csv("data/nps.csv", sep=",")
print(df)

s3_client.upload_file("data/Call Log 230123_175359.csv",
                        "datalake-ib-igti-edc",
                        "data/call_log.csv")