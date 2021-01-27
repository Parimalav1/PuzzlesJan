# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if len(self.storage) <= 0:
            return None
        else:
            value = self.storage.pop(-1)
        self.size -= 1
        return value

    def peek(self):
        return self.storage[-1]

    def isEmpty(self):
        if len(self.storage) <= 0:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.storage}'

# FIFO using 2 stacks


class MyQueue:
    def __init__(self):
        self.size = 0
        self.storage = [Stack(), Stack()]
        # self.stack1 = Stack()
        # self.stack2 = Stack()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        while len(self.storage[1]) > 0:
            value2 = self.storage[1].pop()
            self.storage[0].push(value2)
        self.storage[0].push(value)
        self.size += 1

    # def enqueue(self, value):
    #     if len(self.storage[1]) == 0:
    #         self.storage[0].push(value)
    #     else:
    #         while len(self.storage[1]) > 0:
    #             value2 = self.storage[1].pop()
    #             self.storage[0].push(value2)
    #         self.storage[0].push(value)
    #     self.size += 1

    def dequeue(self):
        while len(self.storage[0]) > 0:
            value2 = self.storage[0].pop()
            self.storage[1].push(value2)
        value = self.storage[1].pop()
        self.size -= 1
        return value


q = MyQueue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.dequeue())
print(q.dequeue())
q.enqueue('D')
q.enqueue('E')
q.enqueue('F')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
