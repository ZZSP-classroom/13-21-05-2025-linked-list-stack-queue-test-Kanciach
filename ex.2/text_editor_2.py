class Stack:
    def __init__(self):
        self.items = []

    def push(self, operation):
        self.items.append(operation)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None