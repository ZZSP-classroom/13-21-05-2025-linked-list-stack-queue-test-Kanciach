class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient : Patient):
        self.queue.append(patient)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None