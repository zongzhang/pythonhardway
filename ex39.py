# -*-coding:utf-8-*-

states = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "Michign's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
print "Michign has: ", cities[states['Michigan']]

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Sorry no Texas"

city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
