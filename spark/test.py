import findspark
findspark.init("C:\Spark\spark-3.1.2-bin-hadoop3.2") #wherever your Spark directory is
import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.sql('''select 'spark' as hello ''')