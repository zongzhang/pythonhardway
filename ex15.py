from sys import argv

script1, filename = argv

txt = open(filename)

print "here're your file %r:" % filename
print txt.read()

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(filename)

print txt_again.read()
