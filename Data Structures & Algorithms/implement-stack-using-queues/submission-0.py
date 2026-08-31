class MyStack:

    def __init__(self):
        self.lists = []

    def push(self, x: int) -> None:
        self.lists.append(x)

    def pop(self) -> int:
        return self.lists.pop()

    def top(self) -> int:
        return self.lists[-1]

    def empty(self) -> bool:
        if len(self.lists) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()