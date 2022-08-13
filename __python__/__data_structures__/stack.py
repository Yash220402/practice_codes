# Stack implementation in python 

# creating stack
def create_stack():
	stack = []
	return stack 

# creating an empty stack
def isEmpty(stack):
	return len(stack) == 0

# adding items into the stack
def push(stack, item):
	stack.append(item)
	print(f"Pushed item: {item}")

# return an element from the stack
def pop(stack): 
	if (isEmpty(stack)):
		return "Stack is empty."

	return stack.pop()

if __name__ == "__main__":
	stack = create_stack()
	push(stack, str(1))
	push(stack, str(2))
	push(stack, str(3))
	push(stack, str(4))
	print("Popped item:", pop(stack))
	print("Stack after popping an element:", str(stack))