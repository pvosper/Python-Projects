people = 30
cars = 30
buses = 45

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
# if neither cars > or < people; ie, if cars == people
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we should take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."