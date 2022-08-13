"""
Algorithm for finding the count of duplicate elements in the array using Binary search
Using binary search find the first and the last occurence of the element to be searched
"""

def FirstOccurrence(array, n):
    start = 0
    end = len(array) - 1

    while (start <= end) :
        mid = int (start + (end-start)/2)

        if (array[mid] == n) :
            if (mid-1 >= 0 and array[mid-1] == n):
               end = mid-1
               continue
            return mid 
        elif (array[mid] < n) :
            start = mid + 1 
        else :
            end = mid - 1 

    return -1  

def LastOccurrence(array, n):
    start = 0
    end = len(array)-1

    while (start <= end):
        mid = int(start + (end-start)/2)

        if (array[mid] == n) :
            if (mid+1 < len(array) and array[mid+1] == n):
               start = mid + 1 
               continue
            return mid 
        elif (array[mid] < n) :
            start = mid + 1 
        else :
            end = mid - 1

    return -1; 


if __name__ == "__main__":
	array = [1, 2, 3, 9, 9, 9, 9, 10, 10, 12, 13]
	# n = int (input("Enter the number : "))
	n = 10

	first_index = FirstOccurrence(array, n)
	last_index  = LastOccurrence(array, n)

	if (first_index == -1 or last_index == -1) :
	    print("Element does not exist")
	else :
	    print(f"First occurrence of {n} is at index: {first_index}")
	    print(f"Last occurrence of {n} is at index: {last_index}")
	    print(f"Total count : {last_index - first_index + 1}") 
