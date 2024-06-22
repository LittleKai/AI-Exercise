class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]


queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)

print(queue.is_full())
print(queue.front())
print(queue.dequeue())
print(queue.front())
print(queue.dequeue())
print(queue.is_empty())