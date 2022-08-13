def fact(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n * fact(n-1)

def strong(num):
	temp = 0
	for i in str(num):
		temp += fact(int(i))

	if temp == num: return "Yes"
	else: return "No" 

if __name__ == '__main__':
	n = 145
	print(strong(n))