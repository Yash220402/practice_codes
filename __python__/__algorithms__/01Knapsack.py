# NAIVE APPROACH
def knapsackNaive(W, wt, val, n):
	"""
	Args:
		W (int) 	= Capacity of the knapsack
		wt (list)   = weights of each item
		val (list)  = value of each item
		n 			= number of items
	"""

	# base case
	if n == 0 or W == 0:
		return 0

	# if weight of the nth item is more than the
	# capacity W of the knapsack
	if (wt[n-1] > W):
		return knapsackNaive(W, wt, val, n-1)

	else:
		tmp1 = knapsackNaive(W, wt, val, n-1)  # No
		tmp2 = val[n-1] + knapsackNaive(W-wt[n-1], wt, val, n-1)  # Yes
		return max(tmp1, tmp2)


def knapsack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    for i in range(n + 1):
        for w in range(W + 1):

            if i == 0 or w == 0:
                K[i][w] = 0
            
            elif wt[i-1] <= w:
            	tmp1 = val[i-1] + K[i-1][w-wt[i-1]]
            	tmp2 = K[i-1][w]

            	K[i][w] = max(tmp1, tmp2)
            
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 


def knapsackMemo(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
 
    if wt[n-1] <= W:
    	tmp1 = val[n-1] + knapsackMemo(wt, val, W-wt[n-1], n-1)
    	tmp2 = knapsackMemo(wt, val, W, n-1)
    	t[n][W] = max(tmp1, tmp2)
    	return t[n][W]

    elif wt[n-1] > W:
        t[n][W] = knapsackMemo(wt, val, W, n-1)
        return t[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
print(knapsackMemo(W, wt, val, n))