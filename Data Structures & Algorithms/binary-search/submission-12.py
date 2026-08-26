class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        i = 0
        if len(nums) < 2 and nums[0] == target:
            return 0
        elif len(nums) < 2  and nums[0] != target: 
            return -1

        while low <= high:
            mid = (low +  high) // 2
            print(f'{low} < {high}, {mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            # if i > 2:
            #     break
            # i += 1

        return -1

        