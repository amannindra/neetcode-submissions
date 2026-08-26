class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set()
        for i in range(len(nums)):
            if nums[i] in l:
                return True
            else:
                l.add(nums[i])
        return False
        