class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [] # [index, number]
        save = [0] * len(temperatures)
        # save = []
        for i in range(len(temperatures)):
            # print(f"stack: {stack}")
            if len(stack) > 0:
            
                # print(f"prev: {stack}")
                # print(f"{temperatures[i]} > {stack[-1][1]}")
                while len(stack) > 0 and temperatures[i] > stack[-1][1]:
 
                    prev_index, prev_temp = stack.pop()
                    # print(f"prev_index: {prev_index}, prev_temp: {prev_temp}")
                    save[prev_index] = i - prev_index
                    # print(f"save[{prev_index}]: {i} - {prev_index}")
    
            stack.append([i, temperatures[i]])
    
        return save