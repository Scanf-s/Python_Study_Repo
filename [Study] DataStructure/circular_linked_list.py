class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class Circular_LinkedList:
    def __init__(self, data):
        self.head = Node(data) # head pointer 정의
        self.tail = self.head # tail pointer 정의 (for push_back)
    
    def push_back(self, data):
        newNode = Node(data) # data를 담을 새 node 생성
        self.tail.next = newNode # tail의 next가 새로운 node를 가리키도록 설정
        newNode.prev = self.tail # 새로운 node가 tail을 가리키도록 설정
        self.tail = newNode # tail을 새로운 node로 변경

    def print_all(self, reversed=False):
        if reversed:
            cur = self.tail
            print("Tail -> ", end="")
            while cur:
                print(cur.data, end="- > " if cur.prev else " -> ")
                cur = cur.prev
            print(" Head")
        else:
            cur = self.head
            print("Head -> ", end="")
            while cur:
                print(cur.data, end = " -> " if cur.next else " -> ")
                cur = cur.next
            print(" Tail")

    def remove_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data and cur.prev: # 현재 지우려는 node가 head가 아닌 경우
                cur.prev.next = cur.next # 현재 지우려는 노드의 이전 노드의 next를 현재 지우려는 노드의 다음 노드를 가리키게 설정
                return
            elif cur.data == data and not cur.prev: # 현재 지우려는 node가 head이면
                self.head = cur.next # 현재 노드의 다음 노드를 head로 설정 
                return
            elif cur.data == data and cur.next: # 현재 지우려는 node가 tail이 아닌 경우
                cur.next.prev = cur.prev # 현재 지우려는 노드의 다음 노드가 가리키고 있는 prev를 현재 지우려는 노드의 이전 노드를 가리키게 설정
                return
            elif cur.data == data and not cur.next: # 현재 지우려는 node가 tail이라면
                self.tail = cur.prev # 현재 노드의 이전 노드를 tail로 설정
                return
            cur = cur.next
        print("Data not found in given list")

if __name__ == "__main__":
    # 1. 리스트 초기화 및 데이터 추가
    myList = Doublely_LinkedList(10)
    print("초기 리스트에 10 추가 후:")
    myList.print_all()
    
    for i in range(20, 31, 10):  # 20부터 30까지 10씩 증가하며 추가
        myList.push_back(i)
    
    # 2. 전체 리스트 출력
    print("\n데이터 추가 후 전체 리스트 (정방향):")
    myList.print_all()
    
    print("\n데이터 추가 후 전체 리스트 (역방향):")
    myList.print_all(reversed=True)
    
    # 3. 특정 요소 삭제
    print("\n20을 삭제 후:")
    myList.remove_element(20)
    myList.print_all()
    
    # 4. 없는 요소 삭제 시도
    print("\n없는 요소 999 삭제 시도:")
    myList.remove_element(999)

