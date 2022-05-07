# coding:utf8
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    spark_conf = SparkConf().setMaster("local[*]").setAppName("wordcount")
    sc = SparkContext(conf=spark_conf)
    # 读取文件
    file_rdd = sc.textFile("../data/input/words.txt")
    # file_rdd = sc.textFile("hdfs://hadoop102:8020/words.txt")
    # 切割单词 存储集合对象
    words_rdd = file_rdd.flatMap(lambda line: line.split(" "))

    word_with_one = words_rdd.map(lambda word: (word, 1))

    result_rdd = word_with_one.reduceByKey(lambda a, b: a + b)

    print(result_rdd.collect())
