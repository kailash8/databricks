#Code - Using dbutils from IDEs such as Pycharm

from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
 
spark = SparkSession. \
    builder. \
    getOrCreate()
 
dbutils = DBUtils(spark)
 
for file in dbutils.fs.ls('dbfs:/mnt/itv-github-db'):
    print(file)
    
