# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use tortoise and rabbit pointers to detect the cycle then 
        #use counter to track the position of tortoise 
        tortoise = head
        rabbit = head 
        pos = 0 
        while tortoise and rabbit and rabbit.next: 
            tortoise = tortoise.next 
            rabbit = rabbit.next.next
            if tortoise == rabbit: 
                tortoise = head
                while tortoise != rabbit: 
                    tortoise = tortoise.next
                    rabbit = rabbit.next
                return tortoise
        
        
        return None
            