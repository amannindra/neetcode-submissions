class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = float('inf')
        
    def push(self, val: int) -> None:
        if val < self.Min:
            self.Min = val
        path = [self.Min, val]
        self.stack.append(path)
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        if len(self.stack) > 0:
            self.Min = self.stack[-1][0]
        else:
            self.Min = float('inf')
        
    
        

    def top(self) -> int:
        return self.stack[-1][1]


    def getMin(self) -> int:
        return self.stack[-1][0]
