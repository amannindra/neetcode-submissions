class Solution:


    def numOfSubarrays(self, arr, k, threshold) -> int:
        ret = 0
        curSum = sum(arr[:k-1])
        
        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                ret += 1    
            curSum -= arr[L]    

        return ret
    
        