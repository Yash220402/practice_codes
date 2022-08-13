#include<iostream>
using namespace std;

int main() {
	
	int i = 1, val = 1;
	
	while (i <= 5) {
		while (i <= 5) {
			int k = 1;
			while ( k <= 5-i ) {
				cout << " ";
				k += 1;
			}
		}
		int j = 1;
		while(j <= i) {
			cout << val << " ";
			j += 1;
			val += 1;
		}
		cout << endl;
		i += 1;
	}
	
	return 0;
}
