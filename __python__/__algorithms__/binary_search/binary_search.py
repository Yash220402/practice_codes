# BINARY SEARCH
from typing import List

def binarySearch(array: List[int], n: int):
	start = 0
	end = len(array)-1

	while (start <=end):
		mid = int((end-start)/2)
		
		if (array[mid] == n):
			return mid
		elif (n > array[mid]):
			start = mid + 1
		else:
		 	end = mid - 1

	return -1


def main():
	array = [3,5,7,11,12,16,17,52,64,101]
	print("Array:", array)
	search_el = [3, 11, 52, 101]

	for i in search_el:
		print("Search element:", search_el[i])
		index = binarySearch(array, search_el[i])
		if (index != -1):
			print("Element found at position:", index)
		else:
			print("Element not found.")


if __name__ == "__main__":
	main()