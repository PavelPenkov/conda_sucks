import requests
from pyspark.sql import SparkSession

def fuck():
    print("Fuck Conda!")

def request():
    r = requests.get("https://google.com")
    print(r.text)

def spark():
    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ("id", "value"))
    df.write.format("parquet").mode("overwrite").save("/tmp/with_conda")
    request()
