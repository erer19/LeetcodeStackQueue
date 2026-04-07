class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, head = None):
        self.head = head

    def push(self, node):
        cur = self.head
        if cur is None:
            self.head = Node(node)
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(node)
        return

class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        prev = self.queue.head
        if prev is None:
            return None
        cur = prev.next
        if cur is None:
            self.queue.head = None
            return prev.data
        while cur.next is not None:
            cur = cur.next
            prev = prev.next
        prev.next = None
        return cur.data

    def top(self) -> int:
        cur = self.queue.head
        if cur is None:
            return None
        while cur.next is not None:
            cur = cur.next
        return cur.data

    def empty(self) -> bool:
        return self.queue.head is None
