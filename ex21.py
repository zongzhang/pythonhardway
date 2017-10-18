def add(a, b):
    print "adding %d + %d " % (a, b)
    return a + b


def subtract(a, b):
    print "subtract %d - %d " % (a, b)
    return a - b


print "let's do some"

age = add(30, 5)
height = subtract(78, 4)

print "Age : %d ,height %d" % (age, height)
