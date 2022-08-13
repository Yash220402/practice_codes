# Get pythagorean triplets that is <= upto

def getPythagoreanTriplets(upto:int):

	# if a,b,c are pythagorean triplets, then (a < b < c)
	for a in range(1, upto):
		b = a + 1;  # b has to be greater than a
		c = b + 1;  # c has to be greater than b

		while (c <= upto):
			c_squared = a*a + b*b
			# increment c till c_squared = a_squared + b_squared holds true for the given value of a and b
			while c*c < c_squared:
				c += 1

			# triplet found
			if c*c == c_squared and c <= upto:
				print(f"{a}\t{b}\t{c}")

			# increment b only after all the values of c are tried for c_squared = a_squared + b_squared for a
			b += 1



def main():
	print("100 Pythagorean Triplets:\n\t")
	print("{a}\t{b}\t{c}\n")
	getPythagoreanTriplets(upto=100)

if __name__ == "__main__":
	main()