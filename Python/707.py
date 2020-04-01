class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None 
    
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None 
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        
        head = self.head
        for i in range(index):
            head = head.next
        return head.val 
    

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.size += 1 
        newHead = ListNode(val)
        newHead.next = self.head
        self.head = newHead
                    
        return             
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.size += 1 
        newTail = ListNode(val)
        head = self.head
        prev = None
        while head:
            prev = head
            head = head.next
        prev.next = newTail
        return 
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return 
        
        if index == 0:
            return self.addAtHead(val)
        
        newNode = ListNode(val)
        head = self.head
        self.size += 1 
        prev = None 
        for i in range(index - 1):
            prev = head
            head = head.next
        
        nxt = head.next
        head.next = newNode
        newNode.next = nxt
        node = self.head
        for i in range(self.size):
            print(node.val)
            node = node.next
        return 
        
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return 
        self.size -= 1 
        if index == 0:
            self.head = self.head.next 
            return 
        
        head = self.head
        prev = None 
        for i in range(index):
            prev = head 
            head = head.next        
        prev.next = head.next
        return 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)