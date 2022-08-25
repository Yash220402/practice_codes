#include <iostream>
using namespace std;

int fibNonMemo(int n) {
	if (n <= 0) {
		return 0;
	} else if (n == 1) {
		return 1;
	} else {
		return fibNonMemo(n-1) + fibNonMemo(n-2);
	}
}

int main() {
	cout << fibNonMemo(5);
	return 0;
}
