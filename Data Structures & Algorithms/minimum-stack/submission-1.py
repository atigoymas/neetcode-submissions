class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        res = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            res.append(self.stack.pop())

        while len(res):
            self.stack.append(res.pop())
        
        return mini
    
        
