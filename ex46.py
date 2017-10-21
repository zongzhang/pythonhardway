# -*-coding:utf-8-*-
from decimal import Decimal

print 0.1 + 0.1 + 0.1 - 0.3

print Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')

x = set('abcde')
y = set('bdxyz')

print 'e' in x

print x - y
print x | y
print x & y
