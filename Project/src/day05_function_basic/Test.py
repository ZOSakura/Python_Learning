def printTest(): #定义函数
    print("这是一个函数")
printTest() #调用函数
def rectangle_area(l, w): #定义有返回值的函数
    #函数可以添加注释
    """
    计算长方形的面积
    :param l: 长
    :param w: 宽
    :return: 面积
    """
    return l * w
help(rectangle_area) #查看函数的帮助文档
print("长方形的面积是:", rectangle_area(10, 5)) #调用函数并输出返回值
def tuple_test(): 
    return 1, 1, 4, 5, 1, 4 #当有多个返回值时，会自动将返回值打包成一个元组
print("返回值是:", tuple_test())
print(type(tuple_test()))