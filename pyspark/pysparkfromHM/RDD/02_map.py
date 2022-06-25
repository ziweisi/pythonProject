# coding:utf8
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    spark_conf = SparkConf().setMaster("local[*]").setAppName("wordcount")
    sc = SparkContext(conf=spark_conf)

    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    # def add(x):
    #      return x*10+5

    # print(rdd.map(add).collect())
    print(rdd.map(lambda x: x * 10 + 5).collect())
