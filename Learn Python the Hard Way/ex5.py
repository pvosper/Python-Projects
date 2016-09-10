# Exercise #5
# %s: String (converts any python object using str()).
# %r: String (converts any python object using repr()).
# %d: Signed integer decimal
print "--------------------------------------------"
print "   "

paul_name = 'Paul Vosper'
paul_age = 55 # not a lie
paul_height = 75 # inches
paul_weight = 210 # lbs
paul_eyes = 'Brown'
paul_teeth = 'White'
paul_hair = 'Brown'

#Python format characters: https://docs.python.org/2.4/lib/typesseq-strings.html

print "Let's talk about %s." % paul_name
	# %s: String (converts any python object using str()).
	# %r: String (converts any python object using repr()).
print "He's %d inches tall (%d meters)." % (paul_height, paul_height * 0.0254) 
	# %d: Signed integer decimal
print "He's %d pounds heavy (that's only %d kilos)." % (paul_weight, paul_weight * 0.453592)
print "Actually he's not that heavy."
print "He's got %s eyes and %s hair." % (paul_eyes, paul_hair)
print "His teeth are usually %s depending on the coffee." % paul_teeth
print "If I add %d, %d, and %d I get %d." % (
	paul_age, paul_height, paul_weight, paul_age + paul_height + paul_weight)
