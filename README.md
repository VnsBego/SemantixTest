## SemantixTest


# Qual o objetivo do comando cache em Spark?

O objetivo do comando cache	é de disponibilizar ao RDD um acesso mais rápido a determinado dado, colocando o mesmo em memória, desta forma quando um RDD tentar fazer uma determinada ação, que já foi feita antes, não terá a necessidade de fazer uma leitura em disco a qual e muito mais custosa em questões de desempenho.

# O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

Pois basicamente com o spark e possível se utilizar da memória para realizar as operações, enquanto no MapReduce se utiliza de leitura e escrita em disco.

# Qual é a função do SparkContext?

	Preparar e abstrair alguns elementos referentes a comunicação e integração das aplicações spark tais como:
	
	Alocação de recursos em gerenciadores de cluster: exp YARN
	
	Setar a configuração do JOB
	
	Configurar os recursos quando o mesmo está utilizando alocação dinâmica.
	
	entre outros.


# Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

São os objetos responsáveis por manipular os dados dentro de uma aplicação spark de forma resiliente(tolerantes a falhas), distribuída( podem estar particionados em diferentes nós do cluster).


# GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

Pois o reduceByKey primeiramente faz um agrupamento com base na (key) com os dados em cada no, e somente depois vai unir as informações coletadas dos nos, diferente do GroupByKey que não faz nenhum agrupamento antes. Graças a isso o GroupByKey precisa olhar para uma quantidade muito maior de dados.

# Explique o que o código Scala abaixo faz

```scala
	val textFile = sc.textFile("hdfs://...")  
	val counts = textFile.flatMap(line => line.split(" ")) 
		.map(word => (word, 1))
		.reduceByKey(_ + _)
	counts.saveAsTextFile("hdfs://...")
```

	Resumidamente: Contabiliza todas as palavras iguais de um arquivo texto coletado do HDFS, e insere o resultado desse processo em um arquivo texto no HDFS.
	
	Aprofundado: O código lê um arquivo texto de um diretório no hdfs, após isso quebra as linhas por " " e gera uma única coleção, a qual contém todas as palavra que estão dentro do arquivo texto, após isso ocorre uma transformação onde cada palavra e transformada em um mapeamento {chave: valor} onde a chave e a própria palavra e tem valor 1, então após isso os valores são agregados(count) a partir das chaves, e finalmentes esses dados são gravados no HDFS em formato texto.
