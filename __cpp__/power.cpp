#include <iostream>
using namespace std;

int power(int a, int b) {
	int i = 1;
	int temp = a;
	
	while (i != b) {
		temp *= a;
		printf("%d -> %d\n", i, temp);
		i++;
	}
	return temp;
}

int main() {
	int a, b;
	
	cout << "Number   (a) = ";
	cin >> a;
	cout << "\nExponent (b) = ";
	cin >> b;
	
	cout << "\nOutput (a raised to the power of b) \n= "
		 << power(a, b) << endl;
	
	return 0;
}
