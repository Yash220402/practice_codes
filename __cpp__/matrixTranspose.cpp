#include<iostream>
using namespace std;

void swap(int &i, int &j) {
	int temp = i;
	i = j;
	j = temp;
}

void transpose(int a[][10], int n) {
	int row = 0;
	while (row < n) {
		for ()
	}
}

int main() {
	int n=3;
	int arr[n][n] = {{1,2,3},{4,5,6},{7,8,9}};
	
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
}
