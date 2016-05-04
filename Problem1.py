# Project Euler solutions by Girish 

# Problem 1 (Status : Success)

sum = 0
	for i in range (1,1000): 
		if i%3==0 or i%5==0:
			sum = sum + i
	print sum

# Output : 233168