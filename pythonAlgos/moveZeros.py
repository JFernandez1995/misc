def moveZeros(arr):
	
	for i in range(len(arr)):
		if arr[i] == 0:
			arr.append(0)
			arr.remove(arr[i])
	return arr


arr = [2, 3, -3, 2,0 , 1, 99, 0]

print(moveZeros(arr))