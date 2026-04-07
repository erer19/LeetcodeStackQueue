class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, node):
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None
        out = self.head
        self.head = self.head.next
        return out.data

    def is_empty(self):
        return self.head is None

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.group:
            self.group[f] = Stack()
        self.group[f].push(Node(val))

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1
        return val
