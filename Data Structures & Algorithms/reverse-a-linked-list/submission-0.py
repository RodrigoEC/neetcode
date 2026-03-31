# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # What we need to do? This questions here is pretty straighr foward
        # because we only need to reverse this linked list. But basically
        # we're going to need to store somewhere some pointers to the elements
        # we're inverting!

        # How should we do it? We're going to iterate through the list and
        # we're going to keep a previous node and a dummy node. The previous
        # represents the head of the already reversed list and the dummy is the
        # head of the list we're currently reversing. Then, what we're going to 
        # do is: We're going to say that the current node next is going to be
        # the previous node, then we'll update the previous to be the current
        # node and the previous next to be the current node.
        #
        # One thing to keep an eye on is that at the end of thi iteration through
        # the list we're not returnin the dummy variable, we're returning the
        # previous variable

        # What structure / algorithm should we use? We're using a linked list

        # What's the time complexity of this approach? O(n)



        previous = None
        dummy = head

        while dummy:

            prevNext = dummy.next
            dummy.next = previous
            previous = dummy
            dummy = prevNext
        
        return previous














