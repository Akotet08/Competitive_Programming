class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if self.size <= index: return -1
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next
        return curr_node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        
                    
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
        cur_node = self.head
        for i in range(self.size - 1):
            cur_node = cur_node.next
        cur_node.next = node
        
        self.size += 1
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index: return 
        if index == 0:
            self.addAtHead(val)
            return
        curr_node = self.head
        for i in range(index - 1):
            curr_node = curr_node.next
        node = Node(val)
        temp = curr_node.next
        curr_node.next = node
        node.next = temp
        
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index: return
        curr_node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return 
        for i in range(index - 1):
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        
        
        self.size -= 1
        
    def print_list(self):
        curr_head = self.head
        print(curr_head.val, end='-->')
        for i in range(self.size-1):
            curr_head = curr_head.next
            if curr_head == None:
                print('None')
                break
            print(curr_head.val, end='-->')
        print()
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)