#include <bits/stdc++.h>
using namespace std;

bool isValidParantheses(string exp) {
	stack<char> s;
	char x;

	for (int i=0; i<exp.length(); i++) {
		if (exp[i] == '(' || exp[i] == '[' || exp[i] == '{') {
			s.push(exp[i]);
			continue;
		}

		if (s.empty()) { return false; }

		// Store the top element
		x = s.top();
		s.pop();

		// check for the opening braces in the stack corresponding 
		// closing bracket
		switch (exp[i]) {
			case ')':
				if (x == '{' || x == '[') { return false; } 
				break;

			case ']':
				if (x == '(' || x == '{') { return false; }
				break;

			case '}':
				if (x == '[' || x == ')') { return false; }
				break;
		}
	}

	// check empty stack
	return (s.empty());
}

int main() {
	string expression = "{{()]}";

	if (isValidParantheses(expression)) {
		cout << "Balanced" << endl;
	}
	else {
		cout << "Unbalanced" << endl;
	}

	return 0;
}