class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        s = []
        for i in range(len(nums)):
            if i == 0:
                l = nums[1:]
            elif i == len(nums):
                l = nums[:len(nums)]
            else:
                l = nums[:i] + nums[i + 1:]
            
            a = 1
            for j in l:
                a *= j
            s.append(a)
        print(s)
        return s