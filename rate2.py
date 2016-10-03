try:
	input = raw_input("Enter Hours : ")
	hours = float(input)

	input1 = raw_input("Enter Rate : ")
	rate = float(input1)

	print rate, hours

	if hours <= 40:
		pay = hours * rate
	if hours > 40:
		pay = rate * 40 + (rate * 1.5 * (hours - 40))
	print pay
	
except:
	print "Error, please enter numeric input"
	quit()

