class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Circular_LinkedList:
    def __init__(self, data):
        self.head = Node(data) # head pointer 정의
        self.head.next = self.head # circular
    
    def push_back(self, data):
        newNode = Node(data)
        if self.head is None: # 리스트가 empty라면
            self.head = newNode
            newNode.next = self.head
        else:
            cur = self.head
            while cur.next != self.head: # head pointer 이전까지 cur 이동
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    def print_all(self):
        if self.head is None:
            print("List is empty")
            return
        
        cur = self.head
        print("Head -> ", end="")
        while True:
            print(cur.data, end = " -> ")
            cur = cur.next
            if cur == self.head:
                break
        print("Head")

    
    def remove_element(self, data):
        if self.head is None:
            print("List is empty")
            return

        cur = self.head
        prev = None # cur보다 한칸 뒤따르는 노드포인터
        while True:
            if cur.data == data:
                if cur == self.head:
                    if cur.next == self.head:  # list에 존재하는 유일한 node를 지우는 경우
                        self.head = None
                    else: # head를 지우기 위해서, 가장 마지막 node를 찾고, 가장 마지막 노드가 head의 다음에 존재하는 node를 가리키게 해야함
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        self.head = cur.next # head를 head의 다음에 있는 node로 설정
                        last.next = self.head
                else: # head가 아닌 노드를 지우는 경우
                    prev.next = cur.next
                return

            prev = cur
            cur = cur.next
            if cur == self.head: # 데이터가 리스트에 존재하지 않는경우 loop 탈출
                break
        print("Data not found in given Linked List")


if __name__ == "__main__":
    myList = Circular_LinkedList(1)
    
    for i in range(2, 12):
        myList.push_back(i)
    
    myList.print_all()

    myList.remove_element(4)
    myList.print_all()
    myList.remove_element(1234)

