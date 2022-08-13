# EUCLID'S GREATEST COMMON DIVISOR FUNCTION

"""
The idea is that the GCD of two nos. remains the same even if you change
the larger no. by its difference with the smaller no.

Example:
 GCD (90, 54) 
 = GCD (90-54, 54) 
 		= GCD (54, 36) 
 			= GCD (36, 18) 
 				= GCD (18, 18) 
 					= GCD (18, 0) = 18
"""
def EuclidGCD_Iterative(a,b):
	if (a < b):  # to make the greatest number as a
		a, b = b, a

	while (b > 0):
		a = a-b
		if (a < b): 
			a, b = b, a

	return a


def EuclidGCD_Recursive(a,b):
	if (b == 0):
		return a
	else:
		return (EuclidGCD_Recursive(b, a%b))

def main():
	a = 90
	b = 54

	print(f"Iterative: GCD({a},{b}) = ", EuclidGCD_Iterative(a,b))
	print(f"Recursive: GCD({a},{b}) = ", EuclidGCD_Recursive(a,b))


if __name__ == "__main__":
	main()