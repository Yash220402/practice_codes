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
	int n; scanf("%d", &n);
	struct student s[n];
	for(int i=0; i<n; i++) {
	    printf("Enter student %d details: \n", i+1);
	    scanf("%d", &s[i].roll);
	    scanf("%s",  s[i].name);
	    scanf("%f", &s[i].cgpa);
	    cout << endl;
	}
	
	for(int i=0; i<n; i++) {
	    printf("Student %d details are: \n", i+1);
	    cout << "ROLL : " << s[i].roll << endl;
	    cout << "NAME : " << s[i].name << endl;
	    printf("CGPA : %.2f\n\n", s[i].cgpa);
	}
	return 0;
}
