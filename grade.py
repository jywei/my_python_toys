gra1 = raw_input(" Enter a number between 0.0 and 1.0 : ")
grade = float(gra1)

if grade >= 0.0 and grade <= 10.0:
	if grade >= 0.9:
    	print "A"

	elif grade >= 0.8:
    	print "B"
    
	elif grade >= 0.7:
    	print "C"
    
	elif grade >= 0.6:
    	print "D"
    
	else:
    	print "F"

else:
    print "Go fuck yourself!"
    quit()