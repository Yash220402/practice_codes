// Structures
#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

struct student {
	int roll;
	char name[50];
	float cgpa;
};

int main() {
	struct student s;
	cin >> s.roll;
	cin >> s.name;
	cin >> s.cgpa;
	
	cout << "ROLL : " << s.roll << endl;
	cout << "NAME : " << s.name << endl;
	printf("CGPA : %.2f", s.cgpa);
	return 0;
}
