class test:
    #类属性(所有实例对象共享的)
    d: int = 114514
    #以双下划线开头结尾的是魔法方法
    #定义魔法方法
    def __init__(self, p):
        #实例属性
        self.p = p
    def __str__(self):
        return f"{self.p}"
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, test):
            return NotImplemented
        return self.p == value.p
    def __lt__(self, value: object):
        if not isinstance(value, test):
            return NotImplemented
        return self.p < value.p
t1 = test(325)
t2 = test(799)
t3 = test(799)
print(t1.__eq__(t2))
print(t2.__eq__(t3))
print(t1.__lt__(t2))
print(t2.__lt__(t3))
#输出实例属性
print(t1.p, t2.p, t3.p)
#输出类属性
print(t1.d, t2.d, t3.d)
#常见的魔法方法
#__init__
#__str__
#__eq__
#__lt__, __le__, __gt__, __ge__