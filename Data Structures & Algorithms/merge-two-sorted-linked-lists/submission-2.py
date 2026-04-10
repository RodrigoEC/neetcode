# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 = [2,4], list2 = [3,5]
        # dummy 
        # res = [0, 1, 1, 2]
        #
        #
        #




        res = ListNode()

        dummy = res
        while list1 or list2:

            if not list1:
                dummy.next = list2
                break
            
            if not list2:
                dummy.next = list1
                break

            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        

        return res.next