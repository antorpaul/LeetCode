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
            head: ListNode = ListNode(array[0])
            currPtr = head
            for i in range(1, len(array)):
                node = ListNode(array[i])
                currPtr.next = node
                currPtr = currPtr.next
            return head
        return None


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = None

        if list1 != None:
            # populate from list1 into result
            currPtr = ListNode(list1.val)
            head = currPtr.next
            node = list1
            while node != None:
                newNode = ListNode(node.val)
                currPtr.next = newNode

                node = node.next
                currPtr = currPtr.next

        if list2 != None:
            # populate from list2 into result
            # make sure sorted
            list2Ptr = ListNode(list2.val)
            if head == None:
                head = list2Ptr
            
            resPtr = head
            while resPtr != None:
                if resPtr.val < list2Ptr.val:
                    newNode = ListNode(list2Ptr.val)
                    newNode.next = resPtr
                    resPtr = newNode
            
        return head
            