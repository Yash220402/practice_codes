#include <iostream>
#include <vector>
using namespace std;

vector<int> aux_vec;

void Merge(vector<int>& vec, int low, int mid, int high) {
	// assigning the left and right value for easier comparison
	int left = low;
	int right = mid+1;
	int aux_index = low;
	
	// pick the smaller no. between the left and right part
	while (left <= mid && right <= high) {
		if (vec[left] <= vec[right]) {
			aux_vec[aux_index] = vec[left];
			aux_index++;
			left++;
		}
		else {
			aux_vec[aux_index] = vec[right];
			aux_index += 1;
			right += 1;
		}
	}

	if (left <= mid) {
		for (int i=left; i <= mid; i++){
			aux_vec[aux_index] = vec[i];
			aux_index++;
		} 
	else {
		for (int i=right; i <= high; i++) {
			aux_vec[aux_index] = vec[i];
			aux_index++;
		}
	}

	// copy the sorted vec to the main vec
	for (int i=low; i <= high; i++) {
		vec[i] = aux_vec[i]
	}
}

void MergeSort(vector<int>& vec, int low, int high) {
	int mid;
	if (low < high) {
		mid = (low + high)/2;
		MergeSort(vec, low, mid);
		MergeSort(vec, mid+1, high);
		Merge(vec, low, mid, high);
	}
}

int main() {
	vector<int> vec = {7, 3, 5, 2, 4, 1, 8, 6, 0, 10, 9};

	// allocate space for the auxiliray vec
	aux_vec.resize(vec.size());

	MergeSort(vec, 0, vec.size()-1);

	cout << "Sorted Numbers: ";
	for (auto& it: vec) {
		cout << it << " ";
	}

	return 0;
}
