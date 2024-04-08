class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            return "Deque is empty"
        result = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return result

    def pop_back(self):
        if self.head is None:
            return "Deque is empty"
        if self.head == self.tail:
            result = self.head.data
            self.head = self.tail = None
            return result
        current = self.head
        while current.next != self.tail:
            current = current.next
        result = self.tail.data
        self.tail = current
        self.tail.next = None
        return result

    def empty(self):
        return self.head is None


if __name__ == '__main__':
    d = Deque()
    for i in range(5):
        d.push_front(i)
    for i in range(5):
        d.push_back(i)

    for i in range(5):
        print("front : ", d.pop_front())
        print("back : ", d.pop_back())

