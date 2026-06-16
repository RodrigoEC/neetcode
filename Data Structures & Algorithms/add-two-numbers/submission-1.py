# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        # What we're going to do:
        #
        # 1 -> 2 -> 3 -> 4
        # 9 -> 9 -> 9
        #
        # 0 -> 2 -> 3 -> 5

        dum1, dum2 = l1, l2
        result = ListNode()
        res_dummy = result
        carry = 0
        while dum1 or dum2:

            val1 = dum1.val if dum1 else 0
            val2 = dum2.val if dum2 else 0

            if carry + val1 + val2 > 9:
                res_dummy.next = ListNode(carry + val1 + val2 - 10)
                carry = 1
            else:
                res_dummy.next = ListNode(carry + val1 + val2)
                carry = 0
            
            res_dummy = res_dummy.next
            if dum1:
                dum1 = dum1.next

            if dum2:
                dum2 = dum2.next
        
        if carry:
            res_dummy.next = ListNode(1)
        return result.next








