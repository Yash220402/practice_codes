#include <bits/stdc++.h>
using namespace std;

int elements(int m[], int r, int c) {
	int total = 0;
	for (int i=0; i<r+1; i++) {
		for (int j=0; j<c+1; j++) {
			total += m[i][j];
		}
	}
	return total;
}

int integralMatrix(int m[], int r, int c) {
	vector<int> res = {};
	for (int i=0; i<r; i++) {
		vector<int> temp {};
		for (int j=0; j<c; j++) {
			// append elements(m, i, j) to temp
		}
		// append elements(m, i, j) to res
	}
	return res;
}

void display(vector<int> m, r, c) {
	for (int i=0; i<r+1; i++) {
		for (int j=0; j<c+1; j++) {
			cout << m[i][j];
		}
		cout << endl;
	}
}

int main() {
	int r=3, c=3;
	vector<int> m = {{1,2,3}, {4,5,6}, {7,8,9}};
	cout << "Original Matrix:\n";
	display(m, r, c);
	vector<int> res = integralMatrix(m, r, c);
	cout << "Resultant Matrix:\n";
	display(m, r, c);
	
	return 0;
}
