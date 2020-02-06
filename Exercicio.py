from pyspark.sql.session import SparkSession
import pyspark.sql.functions as F

#Exemple: C://Users//UserXPTO//Desktop//Projects//Semantix//
FILES_PATH = ""

spark = SparkSession\
    .builder \
    .appName("Semantix Test") \
    .config("spark.master", "local") \
    .getOrCreate()

df = spark.read.option("delimiter", ' ').csv(FILES_PATH + "//")


#TOTAL DE HOSTS UNICOS
df_unic_host = df.select("_c0").distinct()
print(df_unic_host.count())


# #TOTAL DE ERROS 404
df_error404 = df.select("_c6").filter("_c6 == 404")
print(df_error404.count())


# #TOP 5 COM MAIS 404
df_top5_erro404 = df.select("_c0").filter("_c6 == 404")
df_top5_erro404.groupBy("_c0").count().sort("count", ascending=False).show(5, False)


# #QUANTIDADE DE ​​​​ERROS​ ​404 ​​POR ​​DIA
df_top5_erro404 = df.select("_c3").filter("_c6 == 404").withColumn("dmy", F.substring("_c3", 2, 11))
df_top5_erro404.groupBy("dmy").count().sort("dmy", ascending=False).show(62, False)


#TOTAL ​​DE​​ BYTES ​​RETORNADOS
df_sum_bytes = df.agg(F.sum("_c7")).collect()
print(df_sum_bytes)