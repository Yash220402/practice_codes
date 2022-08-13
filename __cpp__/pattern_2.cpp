#include<iostream>
using namespace std;

int main() {
	
	int i = 1, val = 1;
	
	while (i <= 5) {
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
