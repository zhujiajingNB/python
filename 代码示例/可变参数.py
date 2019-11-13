
def add(*numbers):
    print(type(numbers))

a1 = (1, 2, 3, 4,)
print(add(*a1))

a2 = [1, 2, 3, 4]
print(add(*a2))


def add2(**kwargs):
    print(kwargs)

# 只允许key值为字符串类型
dic = {"name": "tom"}
add2(**dic)
