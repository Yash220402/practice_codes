import os 
import sys 

PATH = "C:/Users/Yash/Desktop/fileInput.txt"

def subArraySum(arr, n, s):
	right = 0
	left = 0
	current = 0

	while right < n:
		if current < s:
			current += arr[right]
			right += 1

		if current > s: 
			current -= arr[left]
			left += 1

		if current == s: 
			return left+1, right

	return -1

def main():
	with open(PATH, "r") as inputfile:
		lines = inputfile.readlines()
		n, s = map(int, lines[0].strip().split(" "))
		arr = list(map(int, lines[1].strip().split(" ")))
		print(n, s)
		print(subArraySum(arr, n, s))
				

if __name__ == '__main__': 
	n = 42
	s = 468
	a = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]

	print(subArraySum(a, n, s))
	# main()

