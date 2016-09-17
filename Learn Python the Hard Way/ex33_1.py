# Convert this while loop to a function you can call and replace test number with a variable
# i = 0
numbers = []

def printNumbers(maxNum):
    # i has to be defined here to prevent UnboundLocalError
    # UnboundLocalError: local variable 'i' referenced before assignment
    i = 0

    while i < maxNum:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print "-----"

# newMaxNum = 7
# printNumbers(newMaxNum)
printNumbers(7)

print "The numbers: "

for num in numbers:
    print num