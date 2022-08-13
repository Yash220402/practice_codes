# EULER'S TOTIENT FUNCTION
"""
It computes the count(totatives) of positive int upto N that are coprime to N.
- two int are coprime if their gcd is 1.
"""

def EulersTotient(N):
	# setting initial no. of totatives to N
	totCount = N
	i = 2

	while (i*i <= N):
		if (N%2 == 0):
			totCount = totCount - int(totCount/i)

		while (N%i == 0):
			N = N/i

		i += 1

	if (N > 1): 
		totCount = totCount - int(totCount/N)

	return int(totCount)


def main():
	print("Φ(15) = {} ".format( EulersTotient(15) ))
	print("Φ(12) = {} ".format( EulersTotient(12) ))
	print("Φ(17) = {} ".format( EulersTotient(17) ))
	print("Φ(9) = {} ".format( EulersTotient(9) ))
	print("Φ(98) = {} ".format( EulersTotient(98) ))
	print("Φ(100) = {} ".format( EulersTotient(100) ))


if __name__ == "__main__":
	main()