#include <iostream>
#include <string>
#include <fstream>

//#include<bits/stdc++.h>
using namespace std;

int burgers(int a, int b) {
	if (a > b)
		return b;
	else if (a < b)
		return a;
	else
		return a;
}

void fileHandling() {
	fstream temp;
	// writing into a file
	temp.open("temp.txt", ios::out); // fileName, fileMode
	if (temp.is_open()) {  // check if the file has been successfully opened
		temp << "Hello\n";
		temp << "World\n";
		temp.close();
	}
	
	// appending into a file
	temp.open("temp.txt", ios::app); // fileName, fileMode
	if (temp.is_open()) {  // check if the file has been successfully opened
		temp << "Hello Again\n";
		temp.close();
	}
	
	// reading from a file
	temp.open("temp.txt", ios::in);
	if (temp.is_open()) {
		string line;
		while (getline(temp, line)) {
			cout << endl;
		}
	} 
}

int main() {
	ofstream fout("input.txt");
	string n_temp;
	getline(cin, n_temp);
	
	int n = stoi(ltrim(rtrim(n_temp)));
	fout << n << endl;
	
	fout.close();
}
