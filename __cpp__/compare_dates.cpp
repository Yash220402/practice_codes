// COMPARE DATES
#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

struct date {
	int year;
	int month;
	int date;
};

int main() {
	struct date d1 = {2022, 10, 20};
	struct date d2 = {2022, 10, 20};
	
	if (d1.year==d2.year && d1.month==d2.month && d1.date==d2.date) {
		cout << "YES";
	} else {
		cout << "NO";
	}
	
	return 0;
}
