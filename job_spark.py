from pyspark.sql.functions import mean, max, min, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Uso no AWS as Spark Job

# Ler os dados do enem 2019

enem=(
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter",";")
    .load("s3://datalake-ib-igti-edc/raw-data/enem/")
    )

# Escrever no Datalake em parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-ib-igti-edc/staging/enem")
)