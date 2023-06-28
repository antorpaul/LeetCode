import typing

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current: ListNode = head
        previous: ListNode = None
        remove: ListNode = None
        trail: int = 0
        i: int = 0

        while current:
            previous = remove
            if i - n == 0:
                remove = current
                trail = 0
            if i > n and trail == n:
                remove = remove.next
                trail = 0

            i += 1
            trail += 1
            current = current.next

        if remove and remove.next:
            previous.next = remove.next
        elif remove and previous:
            previous.next = None
        else:
            head = None
