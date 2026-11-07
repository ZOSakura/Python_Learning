t = (1, 1, 4, 5, 1, 4) #元组定义之后不可修改
print(type(t)) #查询元组类型
count = t.count(1) #查询1在元组中出现的次数
print(count)
index = t.index(4) #查询4在元组中第一次出现的索引位置
print(index)
print(t[3])
#组包与解包
a, b, c, d, e, f = t #基础解包
print(a, b, c, d, e, f)
z1, *z2, z3, z4 = t #拓展解包
print(z1, z2, z3, z4)
*z5, z6 = t
z7, *z8 = t
print(z5, z6)
print(z7, z8)
#利用元组快速交换值
i = 10
j = 20
tuple_ji = j, i
i, j = tuple_ji #元组
print(i, j)
print(type(tuple_ji))