class Stack:
    def push(self,x):
        it = self.head
        while it is not NONE:
            it = it.next
        temp = ListNode(x,it)
        it = temp
        it.next = NONE
    def pop(self):
        it = self.head
        while it is not NONE:
            it = it.next
        this = self.head
        while this is not it:
            this = this.next
        return this.value
        this = this.next
    def peek(self):
        it = self.head
        while it is not NONE:
            it = it.next
        this = self.head
        while this is not it:
            this = this.next
        return this.value

class ListNode:
    def _init_(self,val,nxt):
        self.value = val
        self.next = NONE

def main():
    S1 = Stack()
    S2 = Stack()
    S1.push(5)
    S1.push(10)
    S1.push(15)
    S1.push(20)
    #Enqueue operation using stacks
    for node in range(4):
        temp = S1.pop()
        S2.push(temp)
    value = int(raw_input("Enter the value to enqueue\n"))
    S2.push(value)

    #Dequeue opeartion using stacks
    first_element = S2.pop()

    #Front opeartion using stacks
    S2.peek()
    
