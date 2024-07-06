from typing import List, Optional
import timeout_decorator

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA # pointer that starts at a
        b = headB # pointer that starts at b
        
        lenA = 0
        while a != None:
            lenA += 1
            a = a.next
        
        lenB = 0
        while b != None:
            lenB += 1
            b = b.next
        
        diff = lenB - lenA
        skipA = 0
        skipB = 0
        # B is longer than A so B has to skip
        if diff > 0:
            skipB = diff
        # A is longer than B so A has to skip
        if diff < 0:
            skipA = -1 * diff
        
        a = headA
        b = headB
        while skipA != 0:
            a = a.next
            skipA -= 1
        while skipB != 0:
            b = b.next
            skipB -= 1
        
        while a != None and b != None:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None

