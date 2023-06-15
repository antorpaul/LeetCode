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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = None
        tail = None

        if list1 == None and list2 == None:
            return head
        
        l1 = list1
        l2 = list2

        while l1 or l2:
            newNode = ListNode()
            if l1 and l2:
                if l1.val < l2.val:
                    newNode.val = l1.val
                    l1 = l1.next
                else:
                    newNode.val = l2.val
                    l2 = l2.next
            elif l1:
                newNode.val = l1.val
                l1 = l1.next
            elif l2:
                newNode.val = l2.val
                l2 = l2.next
            
            if not head:
                head = newNode
                tail = head
            else:
                tail.next = newNode
                tail = tail.next

        return head
            