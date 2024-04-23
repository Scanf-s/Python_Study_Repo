class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def get(self):
        if self.head is None:
            return "Queue is empty"
        result = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return result

    def empty(self):
        return self.head is None


if __name__ == '__main__':
    queue = Queue()
    for i in range(6):
        queue.put(i)

    while not queue.empty():
        print(queue.get())