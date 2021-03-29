# Insert number from keyboard and add to array

import array as number
import random as random

size=int(input("Please enter size of array: "))

number = [0]

for x in range(size-1):
	n=random.randint(0,1000)
	#print("Number is: ", n)
	#print(n)

	# Add input number to array

	if x == 0:
		number[0]=n
	else:
		#append to array 'number'
		number.append(x)
		number[x]=n
		
#Print all array's elements
print(number)


#Sort elements in array

for i in range (size-2):
	for x in range(size-2):
		y=number[x]
		z=number[x+1]
	
		if y>z:
			number[x]=z
			number[x+1]=y
			continue
	
			
		
#Print all array's elements
print(number)