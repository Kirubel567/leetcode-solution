/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(0, head); 
        ListNode* slow = dummy; 
        ListNode* fast = head; 

        while(fast){
            if(fast->val == val){
                ListNode* temp = fast; 
                ListNode* Next = fast->next;  
                slow->next = Next; 
                fast = Next;    
            }else{
                slow = fast; 
                fast = fast->next; 
               
            } 

        }

        return dummy->next; 
        
    }
};