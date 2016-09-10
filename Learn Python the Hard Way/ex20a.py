from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    # seek bytes, not line
    f.seek(0)

def print_a_line(f):
    print f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)

print "More:"

# seek - bytes, not lines - and readline
current_file.seek(3)
print current_file.readline()

# or just read line directly @ byte
print current_file.readline(2)
# How do you print seek location after a readline?