import random as r

a1=['老','大','丑','傻','黑','肥','胖','矮','白','刚','红','笨','呆','长','短','粗','宽','高','坏','皮','痞','壮']

a2=['一','二','三','四','五','六','七','八','九']

a3=['鬼','幺','户','狗','炮','怪','本','王']

for i in range(100):
   name=r.choice(a1)+r.choice(a2)+r.choice(a3)
   print(name)