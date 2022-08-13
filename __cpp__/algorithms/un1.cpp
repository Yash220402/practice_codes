#include <iostream>
#include <string>
using namespace std;

bool checkRecords(string s) {
    int A=0, L=0;
    for(int i=0; s[i]!='\0'; i++){
        if(s[i] == 'A'){ A++; }
        if(s[i] == 'L'){
            L++;    
        	if(L == 3) return false;
		} else { L = 0; }
    } 
    if(A<2){ return true; }
    
	return false;
}

int main() {
	string s = "PPALLP";
	cout << checkRecords(s);
	return 0;
}
