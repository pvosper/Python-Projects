# Example #3

# ---------------------------------------------------------------------------------
print "++++++++++++++++++++++++++++"

print "I will now count my chickens:"

print "\tHens\t", 25 + 30 / 6 # this does not make sense for chickens!
print "\tRoosters\t", 100 - 25 * 3 % 4
print "\r" # carriage return
print "Now I will count the eggs:"

print "\t", 3 + 2 + 1 -5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print "\t", 3 + 2 < 5 - 7

print "What is 3 + 2?"
print "\t", 3 + 2
print "What is 5-7?"
print "\t", 5 - 7

print "Oh, so that's why it's false."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "\r"
# ---------------------------------------------------------------------------------
print "-----------------------------"

print 2.0 / 0.13579 # Ah, float requires leading zero

print "WTF is '100 - 25 * 3 % 4'"
print "OK, so take 100, right?"
print "- 25 =\t", 100 - 25
print "So this is actually 100 - (25 * 3) =\t", 100 - 25 * 3
print "PEMDAS Parenthesis Exponents Multiplication Division Addition Subtraction"
print "75 / 4 =\t", 75.0 / 4 # \ = continuation character
print "18 * 4 =\t", 18 * 4
print "75 - 72 =\t", 75 - 72
print "3 % 4 =\t", 3 % 4
print "25 * 3 % 4 =\t", 25 * 3 % 4
print "So: 100 - 3 =\t", 100 - 3

print "\r"
# ---------------------------------------------------------------------------------
print "-----------------------------"

# Operator Name Example Result
# + Addition x+y Sum of x and y.
# - Subtraction x-y Difference of x and y.
# * Multiplication x*y Product of x and y.
# / Division x/y Quotient of x and y.
# % Modulus x%y Remainder of x divided by y.
# ** Exponent x**y x**y will give x to the power y
# // Floor Division x/ y The division of operands where the result is the quotient in which the digits after the decimal point are removed.
#  - See more at: http://www.w3resource.com/python/python-operators.php#sthash.ugOyFwUb.dpuf

print "x = 14"
x = 14
print "y = 5"
y = 5
print "x + y ="
print x + y
print "x - y ="
print x - y
print "x * y ="
print x * y
print "x / y ="
print x / y
print "x % y ="
print x % y
print "x ** y ="
print x ** y
print "x // y ="
print x // y

print "\r"
# ---------------------------------------------------------------------------------
# http://mkaz.com/2012/10/10/python-string-format/
print "-----------------------------"

pi = 3.14159
print(" pi = %1.2f " % pi)