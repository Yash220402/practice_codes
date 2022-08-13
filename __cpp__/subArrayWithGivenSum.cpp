/* 
Given an unsorted array A of size N that contains only non-negative integers, 
find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving 
from left to right.
*/
#include <bits/stdc++.h>
using namespace std;

vector<int> subarraySum(int arr[], int n, long long s)
{
    // Your code here
	int left {0};
    int right {0};
    int current_sum {0};
       
    while(right < n){
    	current_sum += arr[right];   
        if(current_sum > s){
            left++;
            right = left;
            current_sum = 0;
            continue;
        }

        if(current_sum == s){
            return {left+1, right+1};
        }
        right++;
    }   
    return {-1};
}

int main() {
	int n = 42;
	int s = 468;
	int a[n] = {135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 
	196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 
	139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134};
	
	vector<int> res;
	res = subarraySum(a, n, s);
	cout << res;
	
	return 0;
}
