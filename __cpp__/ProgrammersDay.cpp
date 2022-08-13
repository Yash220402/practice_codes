// Programmmer's Day
#include <iostream>
using namespace std;

bool checkLeapGreg(int year) {
	if (year%400==0 || (year%4==0 && year%100!=0)) return 1;
	else return 0;
}

bool checkLeapJulian(int year) {
	if (year%4==0) return 1;
	else return 0;
}

int main() {
	int year; scanf("%d", &year);
	if (year > 1918) {
		// after 1918
		if (checkLeapGreg(year) == 1)
			cout << "12.09." << year;
		else
			cout << "13.09." << year;
	}
	else if (year < 1918) {
		// before 1918
		if (checkLeapJulian(year) == 1)
			cout << "12.09." << year;
		else
			cout << "13.09" << year;
	}
	else {
		// ot 1918
		cout << "26.09.1918";
	}
	
	return 0;
}
