# 10.2.3 Triple-quoted strings
# ... For such situations, ``triple-quoted'' strings can be used
# Triple-quoted strings can be surrounded by three single quotes as well,
# 	again without semantic difference.

print " "
print "9" * 80
print " "

# Here's some strange stuff, remember to type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here
With the three double quotes
We'll be able to type as much as we like
Even 4 lines if we want, or 5, or 6
"""