#include<iostream>
#include<vector>

std :: vector<int> auxvec;

// Function to merge the sorted sub-arrays into a bigger array.
void Merge (std :: vector<int>& vec, int low, int mid, int high) {

    int left_index = low;
    int right_index = mid+1;
    int aux_index = low;

    /* Merge elements from vec[low : mid] and vec[mid+1 : high]
                                ^                  ^
                                |                  |
                              left_index       right_index    */

    // Pick the smaller number between the left part and the right part
    while (left_index <= mid and right_index <= high) {
       if (vec[left_index] <= vec[right_index]) {
          auxvec[aux_index++] = vec[left_index++];
       } else {
          auxvec[aux_index++] = vec[right_index++];
       }
    }

    if (left_index <= mid) {
       // There are still some unpicked numbers in the left part
       for (int i = left_index; i <= mid; i++) {
           auxvec[aux_index++] = vec[i];
       }
    } else {
       // There are still some unpicked numbers in the right part
       for (int i = right_index; i <= high; i++) {
           auxvec[aux_index++] = vec[i];
       }
    }

    // Copy numbers from the sorted auxiliary vector into the original vector
    for (int i=low; i<=high; i++) {
        vec[i] = auxvec[i];
    }
}

// MergeSort function splits each sub-array till only a single element is available in the sub-array 
// and then proceeds with the merge of the sub-arrays into a bigger auxiliary array.
void MergeSort (std :: vector<int>& vec, int low, int high) {

    int mid;
    if (low < high) {
       mid = (low + high)/2;
       MergeSort (vec, low, mid); // Recursively splits left half of the array
       MergeSort (vec, mid+1, high); // Recursively splits right half of the array
       Merge (vec, low, mid, high); // Merge left and right half of the array keeping it sorted.
    }
}

int main(){

    std :: vector<int> vec = {7, 3, 5, 2, 4, 1, 8, 6};
    // Allocate space for the auxiliary vector
    auxvec.resize(vec.size());
    MergeSort (vec, 0, vec.size()-1);

    std :: cout << "Sorted numbers : ";
    for (auto& it: vec)
        std :: cout << it << " ";
    return 0;
}

