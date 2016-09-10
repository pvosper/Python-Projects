print " "
print "-16b-" * 16
print " "

from sys import argv

script, filename = argv

print "Opening the file..."
# The most commonly-used values of mode are
# 	'r' for reading
# 	'w' for writing (truncating the file if it already exists)
# 	'a' for appending (...)
# 	If mode is omitted, it defaults to 'r'.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

# http://stackoverflow.com/questions/11584247/how-can-i-simplify-this-series-of-target-write-commands
# %s: String (converts any python object using str()).
target.write("%s\n%s\n%s" % (line1, line2, line3 ))

print "And finally, we close it."
target.close()