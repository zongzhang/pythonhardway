# -*-coding:utf-8-*-

y, z = 1, 2


def all_global():
    global x
    x = y + z


print all_global()
print x + 1
