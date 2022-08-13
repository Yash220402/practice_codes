#include<bits/stdc++.h>
using namespace std;

int fact(int n) {
    if(n == 0 || n == 1) {
        return 1;
    }
    else {
        return n * fact(n - 1);
    }
}

void strong(int num) {
    string s = to_string(num);
    int temp = 0;
    for (int i=0; i<s.size(); i++) {
    	temp += fact(s[i]-'0');
	}
	if (temp == num) {
		cout << "Yes";
	} else {
		cout << "No";
	}
}

int main() {
    strong(145);
    return 0;
}
