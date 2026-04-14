# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        # head = [2,4,6,8]
        #
        # [2,4] and [6,8]
        # [2,4] and [8,6]
        # 
        #
        #
        # 
        #
        #               |
        #         |
        def reverseList(curHead):

            prev = None
            dummy = curHead
            while dummy:
                tempNext = dummy.next
                dummy.next = prev
                prev = dummy
                dummy = tempNext
            
            return prev



        nodes = 0

        dummy = head
        while dummy:
            nodes += 1
            dummy = dummy.next

        print(nodes)

        firstFragment = math.ceil(nodes / 2)
        secondFragment = nodes - firstFragment

        secondHead = head
        n = firstFragment
        prev = None
        while n:
            n -= 1
            prev = secondHead
            secondHead = secondHead.next
        
        prev.next = None
        secondHead = reverseList(secondHead)

        d1, d2 = head, secondHead
        while d1 and d2:

            prevD1Next = d1.next
            prevD2Next = d2.next
            d1.next = d2
            d2.next = prevD1Next
            
            d1 = prevD1Next
            d2 = prevD2Next










