def maxCrossingSum(arr, l, m, h):
    sm = 0
    left_sum = -10000
    
    for i in range(m, l-1, -1):
        sm = sm + arr[i]
        
        if (sm > left_sum):
            left_sum = sm
            
    sm = 0
    right_sum = -10000
    
    for i in range(m+1, h+1):
        sm += arr[i]
        
        if (sm > right_sum):
            right_sum = sm 
            
    
    return max(left_sum + right_sum, left_sum, right_sum)
    
    
def maxSubArray(arr, l, h):
    if (l == h):
        return arr[l]
    
    m = (l+h) // 2
    
    return max(maxSubArray(arr, l, m),
            maxSubArray(arr,m+1, h),
            maxCrossingSum(arr, l, m, h))
            
            
arr = [2, 3, 4, 5, 7]
n = len(arr)
  
max_sum = maxSubArray(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)