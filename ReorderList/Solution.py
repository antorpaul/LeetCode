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
        # populate a stack that contains the list reversed
        nodeStack: list[ListNode] = []
        node: ListNode = head
        length: int = 0
        while node != None:
            nodeStack.insert(0, node)
            node = node.next
            length += 1
        
        # go through list and modify
        node = head
        i: int = 0
        while i < length:
            if i % 2 == 1:
                tmp = ListNode(node.val, node.next)
                node.val = nodeStack.pop(0).val
                node.next = tmp
            
            if i == length - 1:
                node.next = None

            node = node.next
            i += 1