#include <iostream>
#include <string>
using namespace std;

int two_power(int x) {
	int res = 1;
	for(int i=0; i<x; i++) {
		res = res * 2;
	}
	return res;
}

int binary_to_decimal(string s) {
	int n = s.length()-1;
	int decimal_value = 0;
	
	for(int i=n; i>-1; i--) {
		decimal_value = decimal_value + (int(s[n-i]) * two_power(i));
	}
	
	return decimal_value;
}

int main() {
	string s = "1101";
	cout << binary_to_decimal(s);
	
	return 0;
}
