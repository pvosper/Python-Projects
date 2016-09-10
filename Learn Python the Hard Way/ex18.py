# this is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    # r formatter converts any python object to a string using repr().
    # repr() is unambiguous - displays every character in the string
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1 %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Paul", "Vosper")
print_two_again("Paul", "Vosper")
print_one("First!")
print_none()