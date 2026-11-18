PI = 3.1415927
NAME = "魔法ZC目录"

def log_separator1():
    print("- " * 30)
def log_separator2():
    print("+ " * 30)
def log_separator3():
    print("= " * 30)
def log_separator4():
    print("# " * 30)
    
#使用__all__可以控制当调用import *时会导入哪些功能
__all__ = ["log_separator1", "NAME"]
    
#如果执行的是当前文件，则运行如下代码
if __name__ == "__main__" :
    print("当前文件: My_Function")
else :
    print("My_Function 已导入")