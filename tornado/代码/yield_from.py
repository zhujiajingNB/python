# yield from 可以对调用函数main和子生成器gen之间建立双向通道
#还可以解决子生成器stopInternation异常并返回值，
# 但同时当前yield from传值到a时会暂停到下一个yield,如果没有则会在当前函数上产生stopInternation异常
def gen():
    while True:
        a = yield
        if a > 5:
            break
    return a

def g2(gen):
    #注意传值后，会运行到下一个yield，如果没有则会出异常
    a = yield from gen
    print(a)
    # a得到值时，运行到该处3
    yield 1



if __name__ == '__main__':
    g =g2(gen())
    g.send(None)
    for i in range(7):
        g.send(i)