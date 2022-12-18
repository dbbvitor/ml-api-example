"""s3 connector implementation based on pyspark."""

import findspark

findspark.init()

from pyspark import SparkConf
from pyspark.sql import SparkSession


def get_spark():
    """
    Initializes the spark session.
    """
    conf = (
        SparkConf()
        .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .set("spark.sql.execution.arrow.pyspark.enabled", "true")
        .set('spark.jars.packages', 'org.apache.spark:spark-hadoop-cloud_2.13:3.3.1')
        .set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider')
    )

    spark = SparkSession.builder.master("local[1]").appName("MlApiExample").config(conf=conf).getOrCreate()

    return spark
