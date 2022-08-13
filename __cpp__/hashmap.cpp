#include<iostream>
#include<string>
#include<map>
using namespace std;

int main() {
	map<char, char> charPair;
	for (int i=1; i<=26; i++) {
	  	charPair.insert(pair<char, char>(96+i, 123-i));
	}
	
	cout << "Magical Character Pairs: \n";
	for(map<char,char>::iterator it=charPair.begin(); it!=charPair.end(); ++it)
	{
		cout << (*it).first << "->" << (*it).second << endl;
	}
	
	return 0;
}
