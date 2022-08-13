# Find the missing number
def findMissingNumber(array):
	"""Return the missing number in an array of sorted consecutive numbers."""
	diff = array[0]-0

	for i in range(len(array)):
		if (array[i]-i != diff):
			return (diff+i)


def findMultipleMissingNumber(array):
	"""prints the missing numbers in an array of sorted consecutive numbers."""
	diff = array[0]-0

	for i in range(len(array)):
		if (array[i]-i != diff):
			while diff<array[i]-i:
				print(diff+i, end=" ")
				diff += 1


def main():
	array_1 = [1,2,3,4,6]
	array_2 = [1,2,3,5,6,8,9,11]
	# print(findMissingNumber(array=array_1))
	findMultipleMissingNumber(array=array_2)

if __name__ == "__main__":
	main()