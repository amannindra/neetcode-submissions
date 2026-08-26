class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if str(target - nums[i]) in d:
                j = d[str(target-nums[i])]
                if i != j:
                    return [d[str(target-nums[i])], i]
            else:
                d[str(nums[i])] = i
        
                
                
        