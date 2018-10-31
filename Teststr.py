# -*- coding: utf-8 -*-


def maker(n):
    def action(x):
        return x ** n

    return action


f = maker(2)
print(str(f(3)))
