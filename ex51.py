# -*-coding:utf-8-*-
def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


print min2("bb", "aa")
