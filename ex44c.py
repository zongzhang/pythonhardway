# -*-coding:utf-8-*-
class Parent(object):
    def altered(self):
        print "parent altered"


class Child(Parent):
    def altered(self):
        print "Child before"
        super(Child, self).altered()
        print "child after"


dad = Parent()
son = Child()

dad.altered()
son.altered()
