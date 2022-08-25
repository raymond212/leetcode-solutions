class MinStack:
    
    def __init__(self):
        self.stack = collections.deque()
        self.min_stack = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and val > self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()