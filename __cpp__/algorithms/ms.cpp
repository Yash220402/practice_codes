#include<iostream>
#include<vector>

std :: vector<int> auxvec;
void Merge (std :: vector<int>& vec, int low, int mid, int high) {

    int left_index = low;
    int right_index = mid+1;
    int aux_index = low;

    while (left_index <= mid and right_index <= high) {
       if (vec[left_index] <= vec[right_index]) {
          auxvec[aux_index++] = vec[left_index++];
       } else {
          auxvec[aux_index++] = vec[right_index++];
       }
    }

    if (left_index <= mid) {
       for (int i = left_index; i <= mid; i++) {
           auxvec[aux_index++] = vec[i];
       }
    } else {
       for (int i = right_index; i <= high; i++) {
           auxvec[aux_index++] = vec[i];
       }
    }

    for (int i=low; i<=high; i++) {
        vec[i] = auxvec[i];
    }
}
void MergeSort (std :: vector<int>& vec, int low, int high) {

    int mid;
    if (low < high) {
       mid = (low + high)/2;
       MergeSort (vec, low, mid);
       MergeSort (vec, mid+1, high);
       Merge (vec, low, mid, high);
    }
}

int main(){

    std :: vector<int> vec = {7, 3, 5, 2, 4, 1, 8, 6};
    auxvec.resize(vec.size());
    MergeSort (vec, 0, vec.size()-1);

    std :: cout << "Sorted numbers : ";
    for (auto& it: vec)
        std :: cout << it << " ";
    return 0;
}

