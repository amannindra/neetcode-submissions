class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(f"Sorted: {nums}")
        i = 0
        j = 1
        k = len(nums) - 1
        l = []
        while i < len(nums):
            while j < k:
                print("i", i, "j", j, "k", k)

                if nums[i] + nums[j] + nums[k] == 0:
                    print(f"Appending {nums[i]} + {nums[j]} + {nums[j]} = {nums[i] + nums[j] + nums[k]}")
                    print(f"i = {i}, j = {j}, k = {k}")
                    p = [nums[i], nums[j], nums[k]]
                    if p not in l:
                        l.append([nums[i], nums[j], nums[k]])
                    j += 1
                if nums[i] + nums[j] + nums[k] > 0:
                    print(f"Greator {nums[i]} + {nums[j]} + {nums[j]} > {nums[i] + nums[j] + nums[k]}")
                    print(f"i = {i}, j = {j}, k = {k}")
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    print(f"Less than {nums[i]} + {nums[j]} + {nums[j]} < {nums[i] + nums[j] + nums[k]}")
                    print(f"i = {i}, j = {j}, k = {k}")
                    j += 1

            print("______________")
            i += 1
            j = i + 1
            k = len(nums) - 1
        return l
        