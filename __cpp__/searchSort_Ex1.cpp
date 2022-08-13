#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void swap(int *x, int *y) {
	int t = *x;
	*x = *y;
	*y = t;
}

// Selection sort function
void ss(int a[], int n) {
	int i, j, min;
	
	for (i=0; i<4; i++)
	{
		min = i;
		for (j=i+1; j<n; j++) {
			if (a[j]>a[min]) min=j;
		
		swap(a[min], a[i]);
		}
	}
}

/*
int main() {
    // Enter your code here. Read input from STDIN. Print output to STDOUT
    
    int Pucca=0;
    int Garu=0;
    
    int n;
    cin>>n;
    
    int A[n];
    for(int i=0; i<n; i++) {
        cin>>A[i];
    }
    
    for (int i=0; i<n; i++) {
        int index = 0;
        if(i%2 == 0) {
            cin>>index;
            Pucca += A[index];
        }
        else {
            cin>>index;
            Garu += A[index];
        }
    }
    
    if (Pucca > Garu) {
        cout<<"Pucca":
    } else {
        cout<<"Garu";
    }
    
    return 0;
}
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;
    
    int a[n];
    for(int i=0; i<n ; i++) {
        cin>>a[i];
    }
    
    long int p=0, g=0;
    int i=0, j=n-1, f=0;
    
    while(i<=j) {
        if (f==0) {
            if (a[i]>=a[j]) {
                p+=a[i]; i++;
            }
            else {
                p+=a[j]; j--;
            }
            f = 1;
        }
        else {
            if (a[i]>=a[j]) {
                g+=a[i]; i++;
            }
            else {
                g+=a[j]; j--;
            }
            f = 0;
        }
    }
    if (p >= g) {
        cout<<"Pucca";
    } else {
        cout << "Garu";
    }
    
    return 0;
}

