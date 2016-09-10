print " "
print "-13-" * 20
print " "

from sys import argv

# argument variable sys.argv
# The list of command line arguments passed to a Python script
# argv[0] is the script name

script, first, second, third = argv

foo = raw_input("Tap some keys: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", argv[3]

print "Raw: %r argv: %r argv: %r" % (
	foo, script, third)

# Modules, modules, modules
