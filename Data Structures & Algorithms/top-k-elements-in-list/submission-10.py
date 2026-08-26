class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
    
        for i in range(len(nums)):
            if str(nums[i]) in d:
                d[str(nums[i])] += 1
            else:
                d[str(nums[i])] = 1
        print(d)
       
        nums = sorted(d.items(), key=lambda item: item[1], reverse = True)
        nums = list(map(lambda x: x[0], nums))
        print(nums)
        return nums[0:k]