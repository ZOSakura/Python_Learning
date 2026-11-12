num1 = 114514
print(num1)
def test_1():
    #变量名相同时，局部变量在函数内会覆盖全局变量
    #num1 = 10
    #print(num1)
    num2 = 114
    #print(num1) #函数内部可以直接调用全局变量
    global num1
    #不使用局部变量而是使用全局变量进行之后的操作(一般情况下不推荐在函数中直接操作全局变量，这会使代码变得难以维护和修改)
    num1 = 325
    print(num1)
#print(num2) 函数外不能调用函数内的变量
print(num1)
def test_2(a, b, c, d):
    return a+b+c+d
#传递参数的方式:
#位置传参:
print(test_2(1, 2, 3, 4))
#关键字传参:
print(test_2(c=3, d=4, a=1, b=2)) #关键字传参时不需要按顺序写
#混用:
print(test_2(1, 2, d=4, c=3)) #混用时，关键字传参需要写在位置传参的后面
#函数可以定义默认参数
def test_3(a, b, c=3, d=4): #默认参数需要放在正常参数的后面
    return a+b+c+d
print(test_3(1, 2)) #默认有参数的地方若没有参数传入，则会自动使用默认值