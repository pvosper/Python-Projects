# use for loop instead of while
# i = 0
# List [] sequence of arbitrary objects
numbers = []
# incrementValue = 3

def printNumbers(minNum,maxNum,incrementValue):
    # i has to be defined here to prevent UnboundLocalError
    # UnboundLocalError: local variable 'i' referenced before assignment
    i = 0

    # while i < maxNum:
    for i in range(minNum,maxNum,incrementValue):
        print "At the top i is %d" % i
        numbers.append(i)

        # incrementValue can be defined outside of the definition
        # ? NameError: global name 'incrementValue' is not defined
        i = i + incrementValue

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print "-----"

# newMinNum = 3
# newMaxNum = 15

# print newMinNum
# print newMaxNum
# printNumbers(newMinNum,newMaxNum)

printNumbers(7,35,3)

print "The numbers: "

for num in numbers:
    print num