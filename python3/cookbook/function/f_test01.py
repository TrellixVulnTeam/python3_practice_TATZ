# 接受任意数量参数的函数
def avg(first, *rest):
    # loop up sum() and len() param
    return (first+sum(rest))/(1+len(rest))

a = avg(1, 2, 4, 7, 12)
print(str(a))

# 只接受关键词参数的函数
def rev(maxsize, *, block):
    pass

# rev(1024,True)
# rev(1024,block = True)

def mininum(*values,num=None):
    m = min(values)
    if num is not None:
        m = num if num > m else m
    return m

a = 1;
a = mininum(1,2,16,-5,10)
# a = mininum(1,2,16,-5,10,num = 0)
print(a)

# 给函数参数增加元信息
def add(x: int,y: int) -> int:
    return x + y

# add.__annotations__
# help()


# 返回多个值的函数
def myfun():
    # 直接返回一个元组就可以
    return 1, 2, 3

a, b, c = myfun()
print(c,a,b)


# 定义有默认参数的函数
def spam(a,b=42):
    print(a,b)

spam(1,2)# 1 2
spam(1)# 1 42


