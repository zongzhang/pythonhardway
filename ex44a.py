# -*-coding:utf-8-*-
# 隐式继承
class Parent(object):
    def implicit(self):
        print "PARENT implicit"


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
