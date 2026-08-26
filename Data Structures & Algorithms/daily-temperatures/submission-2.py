class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # print(f"temperatures[i]: {temperatures[i]}, index: {i}")
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                # print(f"{stack[-1]} is gone")
                s = stack.pop()
                result[s] = i - s
                # print(f"result: {result}")
        
            stack.append(i)
        return result

        # while i < len(temperatures):
        #     print(f"temperatures[i]: {temperatures[i]}, index: {i}")
        #     if len(stack) > 0:
                
        #         if temperatures[i] > temperatures[stack[-1]]:
        #             print(f"{temperatures[i]} > {temperatures[stack[-1]]}")
        #             temperatures[stack[-1]] = i - stack[-1]
        #             stack.pop()
        #             stack.append(i)
        #         else: 
        #             print(f"{temperatures[i]} < {temperatures[stack[-1]]}")
        #             stack.append(i)
        #     else: 
        #         print(f"Empty Stack: {stack}")
        #         stack.append(i)
        #         print(f"One Stack: {stack}")
        #     print(f'Final Stack: {stack}, temperatures: {temperatures}')
        #     print("!---------!")

        #     i += 1
        # print(f"stack: {stack}")
        return temperatures

