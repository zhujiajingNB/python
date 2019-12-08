"""
生成器，yield关键字修饰的函数，属于迭代器的一种，yield关键字执行时会暂停
生成器，通过传值达到协程的效果

"""

def gen():
    while 1:
        a = yield
        print(a)

if __name__ == '__main__':
    g = gen()
    next(g)
    # g.send(None)
    for i in range(1,11):
        g.send(i)