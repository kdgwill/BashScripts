#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
print "\n\n...closing file", fo.name
# Close opend file
fo.close()
print "Closed or not: ", fo.closed