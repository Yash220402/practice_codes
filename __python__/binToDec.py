def twoPower(x):
	res = 1
	for i in range(x): res *= 2
	return res

def binToDec(s):
	n = len(s)-1
	dec_val = 0

	for i in range(n, -1, -1):
		dec_val += (int(s[n-i])*twoPower(i))

	return dec_val


def main():
	s = "1011"
	print(binToDec(s))  # 11

if __name__ == "__main__":
	main()