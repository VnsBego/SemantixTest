# SemantixTest


## Qual o objetivo do comando cache em Spark?

O objetivo do comando cache	é de disponibilizar ao RDD um acesso mais rápido a determinado dado, colocando o mesmo em memória, desta forma quando um RDD tentar fazer uma determinada ação, que já foi feita antes, não terá a necessidade de fazer uma leitura em disco a qual e muito mais custosa em questões de desempenho.

## O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

Pois basicamente com o spark e possível se utilizar da memória para realizar as operações, enquanto no MapReduce se utiliza de leitura e escrita em disco.

## Qual é a função do SparkContext?

	Preparar e abstrair alguns elementos referentes a comunicação e integração das aplicações spark tais como:
	
	Alocação de recursos em gerenciadores de cluster: exp YARN
	
	Setar a configuração do JOB
	
	Configurar os recursos quando o mesmo está utilizando alocação dinâmica.
	
	entre outros.


## Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

São os objetos responsáveis por manipular os dados dentro de uma aplicação spark de forma resiliente(tolerantes a falhas), distribuída( podem estar particionados em diferentes nós do cluster).


## GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

Pois o reduceByKey primeiramente faz um agrupamento com base na (key) com os dados em cada no, e somente depois vai unir as informações coletadas dos nos, diferente do GroupByKey que não faz nenhum agrupamento antes. Graças a isso o GroupByKey precisa olhar para uma quantidade muito maior de dados.

## Explique o que o código Scala abaixo faz

```scala
	val textFile = sc.textFile("hdfs://...")  
	val counts = textFile.flatMap(line => line.split(" ")) 
		.map(word => (word, 1))
		.reduceByKey(_ + _)
	counts.saveAsTextFile("hdfs://...")
```

	Resumidamente: Contabiliza todas as palavras iguais de um arquivo texto coletado do HDFS, e insere o resultado desse processo em um arquivo texto no HDFS.
	
	Aprofundado: O código lê um arquivo texto de um diretório no hdfs, após isso quebra as linhas por " " e gera uma única coleção, a qual contém todas as palavra que estão dentro do arquivo texto, após isso ocorre uma transformação onde cada palavra e transformada em um mapeamento {chave: valor} onde a chave e a própria palavra e tem valor 1, então após isso os valores são agregados(count) a partir das chaves, e finalmentes esses dados são gravados no HDFS em formato texto.

# Resultados do Codigo

Para utilziar o codigo insira o path onde os arquivos de texto se  encontram na constante FILES_PATH

## Total de Hosts Unicos:
138005

## Total de Erros 404:
20872

## TOP 5 Hosts COM MAIS 404:

```bash
|hoohoo.ncsa.uiuc.edu       |251  |
|piweba3y.prodigy.com       |156  |
|jbiagioni.npt.nuwc.navy.mil|132  |
|piweba1y.prodigy.com       |114  |
|www-d4.proxy.aol.com       |91   |
```

## Quantidade de erros 404 por dia:
```bash
|01/Jul/1995|316  |
|02/Jul/1995|291  |
|03/Jul/1995|470  |
|04/Jul/1995|359  |
|05/Jul/1995|497  |
|06/Jul/1995|640  |
|07/Jul/1995|569  |
|08/Jul/1995|302  |
|09/Jul/1995|348  |
|10/Jul/1995|398  |
|11/Jul/1995|471  |
|12/Jul/1995|470  |
|13/Jul/1995|531  |
|14/Jul/1995|411  |
|15/Jul/1995|254  |
|16/Jul/1995|257  |
|17/Jul/1995|406  |
|18/Jul/1995|465  |
|19/Jul/1995|638  |
|20/Jul/1995|428  |
|21/Jul/1995|332  |
|22/Jul/1995|191  |
|23/Jul/1995|233  |
|24/Jul/1995|328  |
|25/Jul/1995|461  |
|26/Jul/1995|336  |
|27/Jul/1995|336  |
|28/Jul/1995|94   |
|01/Aug/1995|243  |
|03/Aug/1995|303  |
|04/Aug/1995|346  |
|05/Aug/1995|236  |
|06/Aug/1995|373  |
|07/Aug/1995|537  |
|08/Aug/1995|390  |
|09/Aug/1995|279  |
|10/Aug/1995|306  |
|11/Aug/1995|263  |
|12/Aug/1995|196  |
|13/Aug/1995|216  |
|14/Aug/1995|287  |
|15/Aug/1995|327  |
|16/Aug/1995|259  |
|17/Aug/1995|271  |
|18/Aug/1995|256  |
|19/Aug/1995|209  |
|20/Aug/1995|312  |
|21/Aug/1995|305  |
|22/Aug/1995|285  |
|23/Aug/1995|345  |
|24/Aug/1995|420  |
|25/Aug/1995|415  |
|26/Aug/1995|366  |
|27/Aug/1995|367  |
|28/Aug/1995|410  |
|29/Aug/1995|420  |
|30/Aug/1995|571  |
|31/Aug/1995|526  |
```

## Total de bytes retornados
65524319796
