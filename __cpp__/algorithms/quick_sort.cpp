#include <iostream>
#include <algorithm>
using namespace std;

int Partition(int array[], int start, int end) {
	int j = start;
	int pivot = end;
	
	for (int i=start; i<end; i++) {
		if (array[i] < array[pivot]) {
			swap(array[i], array[j]);
			j++;
		}
	}
	swap(array[j], array[pivot]);
	return j;
}

void QuickSort(int array[], int start, int end) {
	int p;
	if (start < end) {
		p = Partition(array, start, end);
		QuickSort(array, start, p-1);  // left partition
		QuickSort(array, p+1, end);  // right partition
	}
}

int main() {
	
	int array[] = {7, 3, 5, 2, 4, 1, 8, 6};
	int n = sizeof(array) / sizeof(array[1]);
	
	cout << "Length of the array = " << n << endl;
	cout << "Unsorted array:" <<endl;
	for (int i=0; i<n; i++) {
		cout << array[i] << " ";
	}
	cout << endl;
	
	QuickSort(array, 0, n-1);
	
	cout << "Sorted array:" <<endl;
	for (int i=0; i<n; i++) {
		cout << array[i] << " ";
	}
	
	return 0;
}
