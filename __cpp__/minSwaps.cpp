#include<iostream>
#include<vector>
using namespace std;

void swap(vector<int> &arr; int i; int j) {
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

int indexOf(vector<int> &arr, int el) {
	for (int i=0; i<arr.size(); i++) {
		if (arr[i] == el) return i;
	}
	return -1;
}

int minSwaps(vector<int> arr, int n) {
	int ans = 0;
	vector<int> temp(arr.begin(), arr.end());
	
	for(int i=0; i<n; i++) {
		if (arr[i] != temp[i]) {
			ans++;
			swap(arr, i, indexOf(arr, temp[i]));
		}
	}
	return ans;
}

int main() {
	vector<int> arr {1,5,4,3,2};
	int n = arr.size();
	
	cout << minSwaps(arr, n);
	return 0;
}
