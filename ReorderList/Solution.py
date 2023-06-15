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
            currPtr = None
            for i in range(0, len(array)):
                newNode = ListNode(array[i])
                if not head:
                    head = newNode
                    currPtr = head
                else:
                    currPtr.next = newNode
                    currPtr = currPtr.next
            return head
        return None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
            Do not return anything, modify head in-place instead.
        """
        switchList: dict[int, ListNode] = {}

        node: ListNode = head
        i: int = 0
        while node != None:
            if i % 2 == 1:
                switchList[i] = node
            
            node = node.next
            i += 1
        
        node = head
        i = 0
        while node != None:
            if i % 2 == 1:
                node.next = switchList[i]
            
            node = node.next
        
        head = node
        print('something')