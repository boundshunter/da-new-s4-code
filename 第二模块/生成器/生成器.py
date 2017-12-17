
# 列表生成式
>>> [i*2 for i in range(10)]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 相当于
list=[]
for i in range(10):
    list.append(i)
print(list)

# 为什么要用列表生成式

生成器和生成式 耗时不同

生成器只申请内存空间，不执行装载数据，准备数据操作

>>> (ix2 for i in range(100))
<generator object <genexpr> at 0x7f57d0311ca8>

生成器只有调用的时候才会生成，不调用不会生成

如何通过其他方式生成一个生成器：
__next__()方法取数据，取不到就会抛一个异常，比如函数值定义了10个值，取了15个值，就会抛异常

可以通过抓取异常：
     try:

    except 异常

生成器特点:  generator
            1、只有在调用时，才会生成相应的数据
            2、__next__方法，生成器取数据，并没有上一个的方法，为了省内存，只保留当前数据 [1,3,5,7.9]，当取到7时，无法返回取到5了。
            3、只记录当前位置，只能向下生成，只有一个__next__()方法 ，在2.7里面，next()
            4、不支持列表切片类操作

            5、一般用循环去调用 next()

用函数来实现生成器

斐波那契数列

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'ok'

fib(20)

>>> def fib(max):
...     n,a,b=0,0,1
...     while n<max:
...         print(b)
...         a,b=b,a+b
...         n+=1
...     return 'ok'
...
>>> fib(20)
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
'ok'