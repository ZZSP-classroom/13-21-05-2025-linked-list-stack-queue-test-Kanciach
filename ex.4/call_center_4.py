class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, call : Call):
        self.items.append(call)

    def denqueue(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def peek(self):
        if self.items:
            return self.items[0]
        return None
    
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