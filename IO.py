'''with open("C:/Users/san/Desktop/2.png", "rb+") as f:
    print(f.read())

with open("C:/Users/san/Desktop/游戏.txt", "w") as f:
    f.write("游戏设定")

from io import StringIO

#内存
f = StringIO()
f.write("aaa")
print(f.getvalue())
#f = StringIO("Helloa!")
#print(f.read())
'''

#操作文件
import os
#查看当前目录
# print(os.path.abspath("."))

# 创建目录
# os.path.join("C:/Users/san/Desktop", "testdir")
# os.mkdir("C:/Users/san/Desktop/testdir")

# 删除
# os.rmdir("C:/Users/san/Desktop/testdir")

# #改名
# os.rename("test.txt","test.py")
# #删除
# os.remove("test.py")

# #创建
# file = open("test.txt", "w")

filename = input("输入文件名字：")
path = os.path.abspath(".")
L = len(path)
def search(filename, path):
     for x in os.listdir(path):
        if os.path.isfile(os.path.join(path, x)) and filename in x:
            print(x, path[L:])

        elif os.path.isdir(os.path.join(path, x)):
            search(filename, os.path.join(path, x))


search(filename, path)
