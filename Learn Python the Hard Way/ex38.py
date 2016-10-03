ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Fridbee", "Corn", "Banana", "Girl", "Boy"]

# assumes len starts <10 and that operation will increase len
while len(stuff) != 10:
    # pop removes specified or last element and returns it
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]

print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print join(' ', stuff)
print '#'.join(stuff[3:5])

