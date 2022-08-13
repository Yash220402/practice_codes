from typing import List

def peakElement(array:List[int], n:int):
	return array.index(max(array))

if __name__ == "__main__":
	array = [1,2,3]
	n = len(array)
	print(peakElement(array, n))