class MyQueue:

    def __init__(self):
        self.stack = []
        self.buffer_stack = []
        
    def move_to_buffer(self):
        if self.buffer_stack:
            return
        while self.stack:
            self.buffer_stack.append(self.stack.pop())
            
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        self.move_to_buffer()
        return self.buffer_stack.pop()
        
    def peek(self) -> int:
        self.move_to_buffer()
        return self.buffer_stack[-1]
        
    def empty(self) -> bool:
        return not self.stack and not self.buffer_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()