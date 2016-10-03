input = raw_input("Enter Hours : ")
h = float(input)

input1 = raw_input("Enter Rate : ")
r = float(input1)

# print rate, hours

def computepay(h, r)
	print "In computepay", h, r

	if h <= 40:
		p = hours * rate
	if h > 40:
		p = r * 40 + (r * 1.5 * (h - 40))
	return p