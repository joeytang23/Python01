#常量名称全大写
__all__ = ["log_separator1", "PI","log_separator3"]
PI = 3.1415926
NAME = "成信大 博崽"

def log_separator1():
    print("- " * 30)#重复30次

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

#测试代码
# __name__ :内置变量表示当前模块的名字
if __name__ == '__main__':
    log_separator1()