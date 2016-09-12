the_count = [1, 2, 11, 4, 5, 6]
fruits = ['apples', 'bananas', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of a for-loop goes through a list
for number in the_count:
    print "this is count %d" % number

for foo in the_count:
    print "this is count %d" % foo

# Same as the above
for fruit in fruits:
    print "a fruit of type: %s" % fruit

# Also we can go through mixed lists, too
# Notice that we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# We can also build lists first start with an empty one
elements = []

# Then use the range functions to do 0 to 5 counts
for i in range(3,11):
    print "Adding %d to the lists." % i
    # append is a function that lists understand
    elements.append(i)

# Now we can print them out too
for i in elements:
    print "Element was: %d" % i