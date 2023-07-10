def selectionSort(arr):
	for i in range(len(arr)):
		#Assume minimum element is at first index
		min_ = i
		#start from the 2nd element and compare it with min by traversing all the element
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_]:
				min_  = j
		#swaping .. by using tuple packing and unpacking
		arr[i], arr[min_] = arr[min_],arr[i]
arr = [2,5,1,9,0]
selectionSort(arr)
print(arr)

