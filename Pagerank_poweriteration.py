import sys
import argparse
import numpy as np
from operator import add
from time import time
from pyspark import SparkContext
from pprint import pprint




def convergence(ro,rl,j,partitions,sc):
  rdd=sc.parallelize(ro)
  rdd=rdd.map(lambda x: (x[1],x[0])).partitionBy(partitions)
  rdd1=sc.parallelize(rl)
  rdd1=rdd1.map(lambda x: (x[1],x[0])).partitionBy(partitions)
  r=rdd.join(rdd1)
  # pprint(r.take(10))
  r=r.mapValues(lambda y: abs(y[1]-y[0]))
  r=r.values()
  val=r.reduce(lambda x,y:x+y)
  print('Iteration:{} Convergence:{}'.format(j,val))
  return val


def pageRank(file,partitions,iterations,sc):
  E=1e-4
  links = sc.textFile(file,partitions)
  # links.count()
  start_time = time()
  links=links.map(lambda x: (x.split('\t')[0],x.split('\t')[1])).distinct().groupByKey().partitionBy(partitions)
  # links.take(3)
  N = links.count()
  # print(N)
  ranks = links.map(lambda node: (node[0],1.0/N))
  ranks = ranks.partitionBy(partitions)
  c_values=[]

  ro=ranks.values().zipWithIndex().collect()

  for j in range(iterations):
    ranks = links.join(ranks).flatMap(lambda x : [(i, float(x[1][1])/len(x[1][0])) for i in x[1][0]]).reduceByKey(lambda x,y: x+y).partitionBy(partitions)
    ranks=ranks.sortByKey()
    rl=ranks.values().zipWithIndex().collect()
    val=convergence(ro,rl,j,partitions,sc)
    c_values.append(val)
    ro=rl

    if(val<E):
      print('Ranks are converged at Iteration {} with value {}'.format(j,val))
    
    if(j==9 or j==19  or j==49 or j==99 or j==149 or j==199 or val<E):
      ranks_list=ranks.collect()
      print('')
      print('Time taken for iteration {}'.format(j+1))
      pprint("--- %s seconds ---" % (time() - start_time))
      print('')
      print('----------10 Top ranked websites--------------')
      ranks=ranks.sortBy(lambda x:x[1],ascending=False)
      pprint(ranks.take(10))
      # ranks.values().sum()
      print('')
      print('----------10 Least ranked websites--------------')
      ranks=ranks.sortBy(lambda x:x[1],ascending=True)
      pprint(ranks.take(10))
      print('')
      print('-------Convergence values---------')
      print(c_values)

    if(val<E):
      break

    
  