# Add another variable to change increment
# i = 0
numbers = []
# incrementValue = 3

def printNumbers(startingValue,maxNum,incrementValue):
    # i has to be defined here to prevent UnboundLocalError
    # UnboundLocalError: local variable 'i' referenced before assignment
    i = startingValue

    while i < maxNum:
        print "At the top i is %d" % i
        numbers.append(i)

        # incrementValue can be defined outside of the definition
        # ? NameError: global name 'incrementValue' is not defined
        i = i + incrementValue

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print "-----"

# newMaxNum = 15
# printNumbers(newMaxNum)
printNumbers(3,27,5)

print "The numbers: "

for num in numbers:
    print num