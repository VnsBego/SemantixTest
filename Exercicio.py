from pyspark import SparkContext

sc = SparkContext("local","SemantixTest")

#ARQUIVOS NA RAIZ DO PROJETO
text_jul = sc.textFile("access_log_Jul95")
text_aug = sc.textFile("access_log_Aug95")


#TOTAL DE HOSTS UNICOS
text_jul_count = text_jul.flatMap(lambda line: line.split(' ')[0]).distinct().count()
text_aug_count = text_aug.flatMap(lambda line: line.split(' ')[0]).distinct().count()

print("Distinct Hosts JUL: %s" %text_jul_count)
print("Distinct Hosts AUG: %s" %text_aug_count)