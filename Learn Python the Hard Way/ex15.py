print " "
print "-15-" * 20
print " "

from sys import argv

script, filename = argv

# open(name[, mode[, buffering]])
# Open a file, returning an object of the file type described in section 
# 	File Objects
# If the file cannot be opened, IOError is raised
# When opening a file, it's preferable to use open() instead of invoking
# 	the file constructor directly.
txt = open(filename)

print "Here's your file %r:" % filename
# file.read([size])
# Read at most *size* bytes from the file
# (less if the read hits EOF before obtaining size bytes)
# If the size argument is negative or omitted, read all data until
# 	EOF is reached
# The bytes are returned as a string object. 
print txt.read()

# print "Type the filename again:"
file_again = raw_input("Filename: ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()