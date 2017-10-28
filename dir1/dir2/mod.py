# -*-coding:utf-8-*-
import sys

print 'in mod.py'
z = 3

print sys.path


class Ca:
    pass


class Cb(object):
    pass


print dir(Ca)
print '--------------------\n'
print dir(Cb)
