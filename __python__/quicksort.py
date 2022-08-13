def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def partition(arr, lo, hi):
	i = lo-1
	pivot = arr[hi]

	for j in range(lo, hi):
		if arr[j] <= pivot:
			i += 1
			# (arr[i], arr[j]) = (arr[j], arr[i])
			swap(arr, i, j)

	# swap the position of the pivot element with the element at
	# the position at i+1
	swap(arr, i+1, hi)

	# return the position from where the partition is done
	return i+1


def quickSort(arr, lo, hi):
	if lo < hi:
		pi = partition(arr, lo, hi)  # pivot
		quickSort(arr, lo, pi-1)
		quickSort(arr, pi+1, hi)


if __name__ == "__main__":
	arr = [3,2,1,5,3,2,6,8,4,7]
	lo = 0
	hi = len(arr)-1

	print(f"Array before sorting: {arr}")
	quickSort(arr, lo, hi)
	print(f"Array after sorting : {arr}")
