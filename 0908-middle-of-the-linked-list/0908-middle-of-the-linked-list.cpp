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
    ListNode* middleNode(ListNode* head) {
        // ListNode* dummy = new ListNode(0, head); 
        ListNode* fast = head; 
        ListNode* slow = head; 
        if(head->next == nullptr) return head; 
        if(!head || !head->next || !head->next->next) return head->next; 
        while(fast && fast->next){
            fast = fast->next->next; 
            slow = slow->next; 
        } 
        return slow; 

        
    }
};