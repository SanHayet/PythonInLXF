#可变参数，*args,args接收的为tuple
#关键字参数，**kw，传入0个或任意数量含参数名的参数，组装为dict
#关键字参数可以用于扩展函数功能
#命名关键字参数，*后的参数为明明关键字参数
def person(name, age, * , city, job):
    pass

#题目其实挺屎的，难为了我的注释
def product(x, *num):
    pro = x
    for n in num:
        pro = pro * n
    return pro
    
    
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')