#include <iostream>
#include <stdio.h>
using namespace std;

// typedef is used to give an alias to a data structure.
typedef unsigned int u;

int main() {
	unsigned int a;
	unsigned int b;
	u c;
	u d;
	u e;
	
	printf("%ld\n", sizeof(a));
	printf("%ld\n", sizeof(b));
	printf("%ld\n", sizeof(c));
	printf("%ld\n", sizeof(d));
	printf("%ld\n", sizeof(e));
}
