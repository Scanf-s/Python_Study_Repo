class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data) # head pointer 정의
        self.tail = self.head # tail pointer 정의 (for push_back)
    
    def push_back(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def print_all(self):
        cur = self.head
        print("Head -> ", end="")
        while cur.next is not None:
            print(cur.data, end = " -> ")
            cur = cur.next
        print("Tail")

    def remove_element(self, data):
        cur = self.head
        if cur == data : # head에 지우고자 하는 데이터가 존재하는 경우
            self.head = cur.next # head pointer를 다음 노드를 가리키게끔 하면 지워짐
            if self.head is None: # head만 존재했었던 node라면 tail도 설정해줌
                self.tail = None
            return
        
        while cur.next is not None: 
            if cur.next.data == data: # cur.next node의 데이터가 target이면
                cur.next = cur.next.next # cur.next가 가리키는 노드를 cur.next.next가 가리키는 노드로 변경
                if cur.next is None: # cur.next가 Null이라면 (노드가 하나밖에 안남았다면)
                    self.tail = cur # tail 재설정
                return
            cur = cur.next
        
        print("Data not found in given Linked List")
        return

if __name__ == "__main__":
    myList = LinkedList(1)
    
    for i in range(2, 12):
        myList.push_back(i)
    
    myList.print_all()

    myList.remove_element(4)
    myList.print_all()
    myList.remove_element(1234)

