def cubedSortedArray(arr):
	arr.sort()
	cubedArray = []
	for element in arr:
		cubedElement  = element**3

		cubedArray.append(cubedElement)


	return cubedArray

array = [3,2,1,4,6,5]

print(cubedSortedArray(array))
