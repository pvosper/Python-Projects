print " "
print "8" * 80
print " "

formatter = "%r %r %r %r"
format_s = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print format_s % (formatter, formatter, formatter, formatter)
print format_s % (format_s, format_s, format_s, format_s)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

print " "