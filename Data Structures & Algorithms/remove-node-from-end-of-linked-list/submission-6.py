# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        # What we need to do?
        # 
        # If we're given a list like this: 
        #  head = [1,2,3,4], n = 2
        # We need to remove the second node from that reversed
        # list, so 3. And then return it again [1,2,4]


        # How should we do it?
        #
        # Reverse, remove and reverse again

        # Time and space complexity:
        # - Time: O(n)
        # - Space: O(1)

        #        1 -> 2 -> 3 -> 4 -> None
        #  None <- 1
        def reverse_list(head):

            prev = None
            cur_node = head

            while cur_node:
                prev_next = cur_node.next

                cur_node.next = prev
                prev = cur_node
                cur_node = prev_next
            
            return prev
        

        new_head = reverse_list(head)
        
        prev = None
        node = new_head
        while n - 1:
            n -= 1
            prev = node
            node = node.next

        if not prev:
            new_head = node.next
        else:
            if prev.next:
                prev.next = prev.next.next
            else:
                prev.next = None
            

        # iterate through 'til n = 0
        return reverse_list(new_head) 






