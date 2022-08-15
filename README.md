# Pagerank
Make sure you have the ‘[web-BerkStan.txt](https://snap.stanford.edu/data/web-BerkStan.txt.gz)’ in your hdfs directory<br/>
1.scp the web-BerkStan.txt file to linux machine 
scp web-BerkStan.txt username@linux.dc.engr.scu.edu:/home/username/<br/>
2. SSH to SCU cluster system<br/>
3.hdfs dfs -copyFromLocal web-BerkStan.txt

### Pagerank_poweriteration.py (Pagerank implementation with power iteration method with partitions)
1.scp Pagerank_poweriteration.py to scu linux machine<br/>
2.From the folder containing Pagerank_poweriteration.py file enter pyspark --master='local[20]'<br/>
3.In pyspark terminal enter the following commands:<br/>
importPagerank_poweriteration as P<br/>
P.pageRank(‘web-BerkStan.txt’,10,20,sc)     //10 partitions, 20-iterations (user can change the input values)

### Pagerank_poweriteration_noPartition.py (Pagerank implementation with power iteration method without partitions)<br/>
1.scp Pagerank_poweriteration_noPartition.py to scu linux machine <br/>
2.From the folder containing Pagerank_poweriteration_noPartition.py file enter pyspark --master='local[20]'<br/>
3.In pyspark terminal enter the following commands:<br/>
import Pagerank_poweriteration_noPartition as PN<br/>
PN.pageRank(‘web-BerkStan.txt’,20,sc) //20-iterations (user can change the input values)

### Pagerank_naive.py (Pagerank naive implementation with partitions)<br/>
1.scp Pagerank_naive.py to scu linux machine <br/>
2.From the folder containing Pagerank_naive.py file enter pyspark --master='local[20]'<br/>
3.In pyspark enter the following commands:<br/>
import Pagerank_naive as N<br/>
N.pageRank(‘web-BerkStan.txt’,10,20,sc)  //10 partitions, 20-iterations (user can change the input values)

### Pagerank_naive_noPartition.py (Pagerank naive implementation without partitions)<br/>
1.scp Pagerank_naive_noPartition.py to scu linux machine <br/>
2.From the folder containing Pagerank_naive_noPartition.py file enter <br/>
pyspark --master='local[20]'<br/>
3.In pyspark enter the following commands:<br/>
import Pagerank_naive_noPartition as NN<br/>
NN.pageRank(‘web-BerkStan.txt’,20,sc) //20-iterations(user can change the input values)
