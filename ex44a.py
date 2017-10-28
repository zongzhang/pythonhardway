# -*-coding:utf-8-*-
# 隐式继承
class Parent(object):
    def __init__(self):
        pass

    def implicit(self):
        print "PARENT implicit"


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
