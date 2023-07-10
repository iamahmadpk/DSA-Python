def insertionSort(arr):
	# suppose first element is sorted, start with the second element
    for i in range(1, len(arr)):
    	# store the second element as Key(we will traverse the array by using key)
        key = arr[i]
        #to get previous element from current
        j = i - 1
        #loop will run until the sorted array's index > j>=0 and the value of arr[j] > key
        while j >= 0 and arr[j] > key:
        	# set the previous value with current
            arr[j + 1] = arr[j]
            j -= 1
        #set the key value to the begginign
        arr[j + 1] = key
       

arr = [4,3,1,5,2]
insertionSort(arr)
print(arr)

#Time and Space Complexity analysis
#Best case: all the array sorted... in this case we need to compare all the element atleast once like 0,1,1,1,1...n-1 = n-1 that we take as O(n)

#Worst Case: the smallest elemet exists at the end of the array.. in this we need to do comparisons like  0,1,2,3...n-1 = n(n-1)/2 => (n"2 n)/2 the element with the highest power is n"2 so O(n"2)

#Average Case: O(n"2)

#Space Complexity: As we are not using any extra space so its O(1)

