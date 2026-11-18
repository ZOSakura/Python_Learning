#导入模块
import random
for i in range(100):
    print(random.randint(1, 100))
#导入模块中某个特定的方法
from random import randint
print(randint(1, 100))
#模块可以添加别名
import math as mt
print(mt.pow(2, 2))

