class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        pre = [0] * n
        post = [0] * n

        pre[0] = nums[0]
        post[-1] = nums[-1]
    
        # print(f"Before Pre: {pre}")
        # print(f"post p]: {post}")

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] *  nums[i]
        
        for j in range(len(nums) - 2, -1, -1 ):
            # print(f"{post[j + 1]} * {nums[j]}")
            post[j] = post[j + 1] *  nums[j]
        
    
        # print(f"pre: {pre}")
        # print(f"post: {post}")
        
        for k in range(0, len(nums)):
            if k == 0:
                nums[k] = post[k+1]
            elif k == len(nums) - 1:
                nums[k] = pre[k-1]
            else:
                nums[k] = pre[k-1] * post[k+1]
        
        # print(f"nums: {nums}")

        return nums