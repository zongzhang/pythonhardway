# -*- coding: utf-8 -*-
def fetcher(obj, index):
    return obj[index]


x = 'spam'
print fetcher(x, 3)

try:
    print fetcher(x, 4)
except IndexError:
    print "异常"

print "come on"
