#匿名函数
#lambda表达式
x=114
y=325
#使用方式
f = lambda a, b : a+b
print(f(x, y))
#或
print((lambda a, b : a+b)(x, y))
data_list = ["Java", "JavaScript", "C/C++", "Rust", "Python", "C#"]
#排序列表内的元素
data_list.sort()
print(data_list)
#通过lambda来让列表内的元素按字符串长度从短到长排序
data_list.sort(key=lambda item : len(item))
print(data_list)
#反转成从长到短
data_list.sort(key=lambda item : len(item), reverse=True)
print(data_list)