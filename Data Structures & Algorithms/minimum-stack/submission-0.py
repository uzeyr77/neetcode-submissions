class MinStack:

    def __init__(self):
        self.data = []
        self.min_elem = None
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
            
        
    def pop(self) -> None:
        self.data.pop()
        self.min_stack.pop()
            

    def top(self) -> int:
        if len(self.data) < 0:
            return None
        else:
            return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
