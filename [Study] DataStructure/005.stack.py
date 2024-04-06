#Stack.py

class Stack:
    # 언더바 2개 : private
    # 언더바 1개 : protected
    __stackDataContainer = []

    def __init__(self):
        self.__stackDataContainer = []
    
    def isEmpty(self):
        if len(self.__stackDataContainer) == 0:
            return True
        else:
            return False
    
    def push(self, numberToPush):
        if numberToPush != None:
            self.__stackDataContainer.append(numberToPush)
        else :
            raise ValueError
        
    def pop(self):
        if not self.isEmpty():
            __toReturn = self.__stackDataContainer[-1]
            del self.__stackDataContainer[-1]
            return __toReturn
        else:
            raise IndexError
    
    def peek(self):
        if not self.isEmpty():
            __toReturn = self.__stackDataContainer[-1]
            return __toReturn
        else:
            raise IndexError
    
    def top(self):
        if not self.isEmpty():
            __toReturn = self.__stackDataContainer[-1]
            return __toReturn
        else:
            raise IndexError
        
    # Shows current elements in stack
    def stackStatus(self):
        __returnString = "\ntop\n"
        for i in range(-1, -len(self.__stackDataContainer) - 1, -1):
            __returnString +=  f'| {self.__stackDataContainer[i]} |\n'
        __returnString += '|___|'
        return __returnString

if __name__ == "__main__":
    myStack = Stack()
    print("0을 스택에 넣어봅시다\n")
    myStack.push(0)
    print("Stack.top() -> ", myStack.top(), "\n")

    print("1부터 10까지 스택에 넣어줍시다\n")
    for i in range(1, 11):
        myStack.push(i)

    print("Stack.top() -> ", myStack.top())

    print("스택의 현재 구조는 다음과 같습니다\n")
    print(myStack.stackStatus())

    print("peek은 pop과 달리, element를 삭제하지 않습니다.\n")
    print(myStack.peek())
    print(myStack.stackStatus())

    print("\n이제 5회 pop해봅시다")
    for i in range(5):
        myStack.pop()
    print(myStack.stackStatus())