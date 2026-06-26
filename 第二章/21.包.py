#1.导入模块
# import utils.my_fun
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()
#
# from utils import my_fun
# my_fun.log_separator3()
# #继续from utils import * 导入包下的模块，需要在__init__.py里面添加__all__=[]
# from utils import *
# my_fun.log_separator4()
# my_fun.log_separator2()
#导入具体功能
from utils import my_fun
from 第二章.utils.my_fun import log_separator3,log_separator4
my_fun.log_separator3()