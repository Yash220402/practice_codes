#include<iostream>
using namespace std;

int main() {
	
	int val, count = 1, sum = 0;
	cout << "Enter the value till which you want the sum: ";
	cin >> val;
	
	while (count <= val) {
		sum = sum + count;
		count = count + 1;
	}
	
	cout << "Sum of nos. from 1 to " << val << " = "<<sum;
	
	return 0;
}
