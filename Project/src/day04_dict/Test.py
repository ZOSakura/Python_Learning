dict1 = {"逸一时误一世":114514, "逸久逸久罢已零":1919810, "苦也，这也言周":325} #定义字典
dict0 = {} #定义空字典
print(type(dict1))
#Key可以是各种类型
dict2 = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九"}
dict3= {(1, 2): "元组", True: "布尔值", 3.14: "浮点数"}
#但是Key不能是可变类型，如列表、字典等
#dict4 = {[114, 514]:325, {"舟":325}}
print(dict1["苦也，这也言周"])
dict1["苦也，这也言周"] = 325799
print(dict1["苦也，这也言周"])
print(dict1.get("逸一时误一世")) #通过Key获取值，如果Key不存在则返回None
print(dict1.get("逸一时误一世", -1)) #默认值可以指定
print(dict1.keys()) #获取所有的Key
print(dict1.values()) #获取所有的Value
print(dict1.items()) #获取所有的键值对
print(dict1.pop("逸久逸久罢已零")) #删除指定的键值对(返回删除的Key对应的值)
dict1["67":67] = 67 #添加键值对
del dict1["67":67] #删除指定的键值对
print("\n")
#通过获取每一个Key去遍历字典
for key in dict1.keys():
    print(f"{key}: {dict1[key]}")
count = 0
print("\n")
#通过获取每一个键值对遍历字典
for item in dict1.items():
    print(f"{item[0]}: {item[1]}")
    if count == len(dict1) - 1:
        print(type(item)) #键值对的类型是元组
    count += 1