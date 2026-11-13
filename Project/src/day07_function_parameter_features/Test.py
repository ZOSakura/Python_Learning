#使用不定长参数的函数
#基于位置传递的不定长参数
def test_1(*args): #一个*加具体的形参名称(不一定要叫args)
    #通过位置传参传进来的参数会被封装成元组
    print(type(args))
    min_num = min(args)
    max_num = max(args)
    avg_num = round(sum(args)/len(args), 1)
    print(min_num, max_num, avg_num)
    print("\n")
test_1(1, 1, 4, 5, 1, 4)
test_1(114514, 1919, 810)
test_1(325, 799)
#使用两个*加具体的形参名称时，可以接收基于关键字传输的参数
def test_2(*args, **kwargs):
    #通过关键字传参传进来的参数会被封装成字典(在封装的字典中，关键字是Key，值是Value)
    print(type(args))
    print(type(kwargs))
    print(sum(args))
    dict_sum = 0
    for item in kwargs.items():
        dict_sum += item[1]
    print(dict_sum)
    print("\n")
test_2(1, 3, 5, 提丰=799, 魔法ZC目录=325)
#也可以将其他函数作为参数传入(此处oper是一个函数)
def test_3(a, b, c, oper):
    oper(a, b, c)
test_3(325, 799, 2026, test_1)