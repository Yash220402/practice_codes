# QUICK SORT
from typing import List  # for annotations

# start and end are indexes

def partition(array:List[int], start:int, end:int):
	j = start
	pivot = end  # last element is the pivot value

	for i in range(start, end):
		if (array[i] < array[pivot]):
			# swap array[i] with array[j]
			array[i], array[j] = array[j], array[i]
			j += 1  # increment the value of j to keep track of the position of the pivot value

	# Swap the value at pivot with the value at array[j]
	array[j], array[pivot] = array[pivot], array[j]
	return j


def quickSort(array:List[int], start:int, end:int):
	p = None  # tracks partition - the index of the pivot

	if (start < end):
		p = partition(array, start, end)
		quickSort(array, start= start, end= p-1)
		quickSort(array, start= p+1, end= end)


def main():
    array = [7, 3, 5, 2, 4, 1, 8, 6]
    print("Unsorted Array:\n{}".format(array))
    
    quickSort(array=array, start=0, end=len(array)-1)
    print("\nSorted array:\n{}".format(array))


if __name__ == "__main__":
	main()