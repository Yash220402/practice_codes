#include <iostream>
#include <stdlib.h>
using namespace std;

#define MAX 10  // defining the maximum size of the stack
int size = 0;  // will be used to store size of the stack

// Creating a stack
struct stack {
	// creating a structure with an array and a variable 'top' pointing 
	// at the topmost value of the stack
	int items[MAX];
	int top;
};
typedef struct stack st;  // give an alias to the structure 'stack'

void createEmptyStack(st *s) {
	// top represent the empty stack the pointer s will point at top 
	// which holds the value of -1
	s->top = -1;
}

// Check if the stack is full
int isFull(st *s) {
	// return true if s->top has the max value else false
	if (s->top == MAX-1) return 1;
	else return 0;
}

// check if the stack is empty
int isEmpty(st *s) {
	// return true if s->top has -1 else false
	if (s->top == -1) return 1;
	else return 0;
}

// add elements into the stack
void push(st *s, int newItem) {
	if (isFull(s)) {
		cout << "Stack full.";
	} else {  // if stack is not full
		s->top++;  // increment the position of top
		s->items[s->top] = newItem;  // insert the value at new top position
	}
	size++;  // increment indicates the size of the stack has increased
}

// remove element from the stack
void pop(st *s) {
	if (isEmpty(s)) {
		cout << "\n Stack empty \n";
	} else {
		// if stack not empty, pop the item top is pointing at
		cout << "Item popped = " << s->items[s->top];
		s->top--;  // by reducing the index where top is pointing
	}
	size--; 
	cout << endl;
}

// Print elements of stack
void printStack(st *s) {
	printf("Stack: ");
	for (int i=0; i<size; i++) {
		cout << s->items[i] << " ";
	}
	cout << endl;
}

int main() {
	int ch;
	st *s = (st *)malloc(sizeof(st));
	
	createEmptyStack(s);
	
	push(s, 1);
	push(s, 2);
	push(s, 3);
	push(s, 4);
	
	printStack(s);
	
	pop(s);
	
	cout << "\nAfter popping out\n";
	printStack(s);
}
