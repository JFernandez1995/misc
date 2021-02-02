'''
def roundTrip(D,R):
	smallestCost = float('inf')
	for i in range(len(D)-1):
		for j in range(i,len(R)-1):
			currentCost = D[i] + R[j]
			if currentCost < smallestCost:
				smallestCost = currentCost
			
	return smallestCost 

D = [10,8,9,11,7]
R = [8,8,10,7,9]   

print(roundTrip(D,R))
'''



'''

def roundTrip(D,R):

	RMinimumValue = min(R) # O(n). We fin the minimum value of the 'R' array
	RMinimumPosition = R.index(RMinimumValue) #O(n). We find the position ,which is our constraint
	
	smallestCost = float('inf')	
	for i in range(RMinimumPosition-1): #O(n) We find the minumum cost
		currentCost = D[i] + RMinimumValue
		if currentCost < smallestCost:
			smallestCost = currentCost
	return smallestCost 

'''




def roundTrip(D,R):

	R.reverse()

	for x in range(len(R)-1):
		if R[x]<R[x+1]:
			R[x+1] = R[x]

	R.reverse()


	for x in range(len(R)-1):
		minimumIdx = x
		if R[x]!=R[x+1]:
			break

	RMinimumValue = R[minimumIdx]

	
	smallestCost = float('inf')	
	for i in range(minimumIdx-1): #O(n) We find the minumum cost
		currentCost = D[i] + RMinimumValue
		if currentCost < smallestCost:
			smallestCost = currentCost
			
	return smallestCost


D = [10,8,9,11,7]
R = [8,8,5,1,9]  

print(roundTrip(D,R))

