class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        total = 0
        while i < j:

            max_height = heights[i]
            if heights[i] > heights[j]:
                max_height = heights[j]
            # print(f"max height: {max_height}")

            width = j - i
            # print(f"width: {width}")

            if width * max_height > total:
                # print(f"{width * max_height} > {total}")
                total = width * max_height

            if heights[i] > heights[j]:
                j -= 1
            else: 
                i += 1
        return total

            
            
            