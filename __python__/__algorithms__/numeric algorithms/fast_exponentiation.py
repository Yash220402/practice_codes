# FAST EXPONENTIATION
"""
If the power is even, then the base would be multiplied with itself ( power / 2 ) times.
Example : 3^2 = ( 3 * 3 )^(2/2) = ( 3 * 3 )^1 = 9

If the power is odd ( and greater than 1 ) then the base would be used in the multiplication with the result once and then it would be multipled with itself
(power-1) times.
Example : 3^3 = 3.( 3 )^2 = 3.(3 * 3)^(2/2) = 3.(3 * 3)^1 = 27
"""

def recExpo(base, power):
	result = 0
	if (power == 0): return 1
	if (power == 1): return base
	elif (power == 2): return base * base

	if (power%2 == 0):  # when power is even and greater than 2
		result = recExpo(base, power//2)
		return result * result
	else:  # when the power is odd
		return base * recExpo(base, power-1)


def fastExpo(base, power):
	result = 1
	while (power > 0):
		if (power%2 == 0):
			result = result * base

		base *= base
		power //= 2

	return result


def bitwise_fastExpo(base, power):
	result = 1
	while (power > 0):
		if (power & 1 == 1):
			result *= base
		base *= base
		power >>= 1
	return result


def main():
	print("Base: 2, Power: 32 i.e (2^32):", recExpo(2, 32))	
	print("Base: 2, Power: 44 i.e (2^44):", fastExpo(2, 44))
	print("Base: 2, Power: 63 i.e (2^63):", bitwise_fastExpo(2, 63))	

if __name__=="__main__":
	main()