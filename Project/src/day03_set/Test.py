s = {"325", "114514", "1919", "810", "325"} #集合: s无序，不可重复，可修改
print(s) #自动去重
print(type(s))
d = {}
print(type(d)) #这样定义出来的并不是集合set，而是字典dict
st = set() #这样定义出来的才是集合set
print(type(st))
s.add("67") #添加元素
print(s)
s.remove("1919") #删除元素(如果元素不存在会报错)
s.remove("810")
print(s)
s.discard("1919") #删除元素(如果元素不存在也不会报错)
print(s)
print(s.difference({"325"})) #求差集
print(s.intersection({"114514", "67"})) #求交集
print(s.union({"1145141919810", "逸一时误一世"})) #求并集
sd = s.copy() #复制集合
for i in range(3):
    print(sd.pop()) #随机删除一个元素(返回的是被删除的元素)
print(sd) #被删除的元素不在集合中
print(s.clear()) #清空集合