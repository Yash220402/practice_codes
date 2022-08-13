#include <iostream>
#include <stdio.h>
using namespace std;

// slow
int fact(int x) {
	int res = x;
	for (int i=x-1; i>0; --i) {
		res = res * i;
	}
	return res;
}

int main() {
	cout << fact(5);
	return 0;
}
