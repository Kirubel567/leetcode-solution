# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev, curr = dummy, head 

        while curr and curr.next: #this is as we want a pair inorder to swap 
            #save some pointers first we need the next pair, and the next node to swap 
            nextPair = curr.next.next 
            toSwap = curr.next 

            #swap 
            curr.next = nextPair 
            toSwap.next = curr
            prev.next = toSwap #make the second node the head or the start of the pair

            #move the ptrs 
            prev = curr 
            curr = nextPair 
        
        return dummy.next 
        