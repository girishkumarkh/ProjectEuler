# Project Euler solutions by Girish 

# Problem 2 (Status : Success)

sum = 0
	first = 1
	second = 2
	temp = 0
	while second<4000000:
		if (second%2 == 0):
			sum = sum + second
		temp = first + second
		first = second
		second = temp
	print sum

# Output : 4613732