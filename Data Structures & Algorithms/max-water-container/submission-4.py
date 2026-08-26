class Solution:
    def maxArea(self, heights) -> int:
        left = 0
        right = len(heights) - 1
        highest = 0
        area = 0
        while left < right:
            low = min(heights[left], heights[right])
            # print(f"heights[{left}]: {heights[left]}, heights[{right}]: {heights[right]}, low: {low}")
            # print(f"max({low*low}, {highest})")
            
            
            # if low * (right - left) > area:
            highest = max(low * (right - left), highest)
                # area = low * low * (right - left)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return highest