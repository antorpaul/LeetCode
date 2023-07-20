# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def createList(array: list):
        if len(array) >= 1:
            head: ListNode = None
            current = None
            for i in range(0, len(array)):
                newNode = ListNode(array[i])
                if not head:
                    head = newNode
                    current = head
                else:
                    current.next = newNode
                    current = current.next
            return head
        return None

    def addNode(self, val: int):
        """ Adds a node to LinkedList """
        current = self
        newNode: ListNode = ListNode(val, None)
        if current:
            while current != None:
                if current.next == None:
                    current.next = newNode
                    current = current.next
                current = current.next
        else:
            head = newNode

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        pass