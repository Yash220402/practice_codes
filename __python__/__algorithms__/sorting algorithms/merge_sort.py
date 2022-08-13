# MERGE SORT
from typing import List

def mergeSort(aux_array:List[int], array:List[int], low:int, high:int):
    if (low < high):
        mid = int((low + high)/2)
        mergeSort(aux_array, array, low, mid)  # recursively splits left half
        mergeSort(aux_array, array, mid+1, high)  # recursively splits right half
        merge(aux_array, array, low, mid, high)  # merge the left and right sorted halves


def merge(aux_array:List[int], array:List[int], low:int, mid:int, high:int):
    # assigning the left and right values for easier comparison
    left = low 
    right = mid+1
    aux_index = low
    # Pick the smaller number between the left part and the right part
    while (left <= mid and right <= high):
        if (array[left] <= array[right]):
            aux_array[aux_index] = array[left]
            aux_index += 1
            left += 1
        else:
            aux_array[aux_index] = array[right]
            aux_index += 1
            right += 1
        # print(aux_array)

    if (left <= mid):
        for i in range(left, mid + 1):
            aux_array[aux_index] = array[i]
            aux_index += 1
    else:
        for i in range(right, high + 1):
            aux_array[aux_index] = array[i]
            aux_index += 1
        
    # copy the sorted aux_array to the main array
    for i in range(low, high+1):
        array[i] = aux_array[i]


def main():
    array = [7, 3, 5, 2, 4, 1, 8, 6, 0, 10, 9]
    print("Unsorted array:\n{}".format(array))
    
    # Allocate space for the auxiliary vector
    aux_array = [None] * len(array)
    
    mergeSort(aux_array=aux_array, array=array, low=0, high=len(array)-1)
    print("\nSorted array:\n{}".format(array))

if __name__ == "__main__":
    main()