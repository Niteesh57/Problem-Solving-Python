class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(val)
        self.min.sort()

    def pop(self) -> None:
        if self.stack != []:
            x = self.stack.pop()
            self.min.remove(x)

    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]
    def getMin(self) -> int:
        return self.min[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()