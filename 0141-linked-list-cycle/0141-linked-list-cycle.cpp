/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* tortoise = head; 
        ListNode* rabbit = head; 
        if(head == nullptr) return false;
        if(head->next == nullptr) return false;  

           while(rabbit && rabbit->next){
            tortoise = tortoise->next; 
            rabbit = rabbit->next->next; 
            if(rabbit == nullptr) return false; 
            if(rabbit == tortoise) {return true;}
        }
        
        return false; 
        
    }
};