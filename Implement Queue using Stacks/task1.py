class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, head = None):
        self.head = head

    def push(self, node):
        node.next = self.head
        self.head = node

    def pop(self):
        out = self.head
        self.head = self.head.next
        return out.data

    def empty(self):
        return self.head is None

class MyQueue:
    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        self.stack.push(Node(x))

    def pop(self) -> int:
        prev = self.stack.head
        if prev is None:
            return None
        cur = prev.next
        if cur is None:
            out = self.stack.pop()
            return out
        while cur.next is not None:
            cur = cur.next
            prev = prev.next
        prev.next = None
        return cur.data

    def peek(self) -> int:
        cur = self.stack.head
        if cur is None:
            return None
        while cur.next is not None:
            cur = cur.next
        return cur.data

    def empty(self) -> bool:
        return self.stack.empty()
