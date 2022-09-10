def minStepsRecur(height, l, r, h):
    if l >= r:
        return 0;

    m = l
    for i in range(l, r):
        if height[i] < height[m]:
            m = i

    return min(r - l,
            minStepsRecur(height, l, m, height[m]) +
            minStepsRecur(height, m + 1, r, height[m]) +
            height[m] - h)
 

def minSteps(height, N):
    return minStepsRecur(height, 0, N, 0)


if __name__ == "__main__":
    n = 5
    coins = [1,2,3,4,5]
    target = 7
    
    print(minSteps(coins, n))