"""
Prints out every line (there will be 99)
Do not type out all the numbers into a list (use range(0,90)
	for every number in that range, 
		list99 = range(0,90)
		for number in list99:
			if number <=98:
				print "%d bottles of beer on the wall, %d bottles of beer!\n Take one down... etc" % (number, number)
			elif number == 99:
				print "%d bottle of beer on the wall, %d bottle of beer!\n There's no more." % (number, number)
			else:
				print "There was a problem."
"""

list99 = reversed(range(1,100))
for number in list99:
	if number == 1:						# Remember when the first one of these statements test as true, the program stops at that if statement
		print "%d bottle of beer on the wall, %d bottle of beer!\n There's no more." % (number, number)

	elif number <=99:
		print "%d bottles of beer on the wall, %d bottles of beer!\n Take one down... etc" % (number, number)
	
	else:
		print "There was a problem. number was %r" % number