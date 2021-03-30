# Insert number from keyboard and add to array

import array as number

number = [0]

for x in range(10):
	n=input("Please enter number: ")
	print("Number is: ", n)
	#print(n)

	# Add input number to array

	if x == 0:
		number[0]=n
	else:
		# extend 'number'
		number.append(x)
		number[x]=n
	
	
#Print all array's elements
print(number)

#Sort elements in array

for i in range (9):
	for x in range(9):
		y=number[x]
		z=number[x+1]
	
		if y>z:
			number[x]=z
			number[x+1]=y
			continue
	
		

		
		
#Print all array's elements
print(number)