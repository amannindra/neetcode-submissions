class Solution:
    def findMin(self, nums):
        print(nums)
        lowest = 99999
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
           
            # print(f"{mid} = ({left} + {right}) // 2")
            if nums[left] < nums[right]:
                lowest = min(lowest, nums[left])
                break
                

            mid = (left + right) // 2
        
            lowest = min(nums[mid], lowest)
            # if nums[mid] >= nums[left]:
            #     left = mid + 1
            # else:
            #     right = mid - 1
            if nums[mid] > nums[right]:
                print(f"right = {mid -1}")
                left = mid + 1
                print(f"{nums[mid]} > {nums[right]}, mid = {mid}, right {right}, left = {left}")

            else:
                right = mid - 1
                print(f"{nums[mid]} < {nums[right]}, mid = {mid}, right {right}, left = {left}")
                # print(f"left = {mid + 1}")
                right = mid - 1
        
        if nums[0] < lowest:
            return nums[0]
        
        return lowest



        