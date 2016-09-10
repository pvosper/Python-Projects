# removing print statements & needless interaction

from sys import argv
# from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line, how?
# in_file = open(from_file); indata = in_file.read()
# indata = in_file.read(); in_file = open(from_file)
# indata = open(from_file).read()

indata = open(from_file).read()

out_file = open(to_file, 'w') # mode = writing
out_file.write(indata)

# python does not actually write the file to disk until
# a) you execute output.close()
# b) end session

out_file.close()