#导入包
import utils.My_Function
utils.My_Function.log_separator1()
#导入模版
from utils import My_Function
My_Function.log_separator2()
#导入包中的某些特定模块(使用这种方式需要在__init__.py文件中添加__all__)
from utils import *
print(My_Var.PI)
print(My_Var.NAME)