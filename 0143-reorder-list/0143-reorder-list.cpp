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
    void reorderList(ListNode* head) {
        ListNode* fast = head; 
        ListNode* slow = head; 

        while(fast && fast->next){
            slow = slow->next; 
            fast = fast->next->next; 
        }
        
        ListNode* before = nullptr; 
        ListNode* temp = slow->next; 
        ListNode* after = temp; 

        while(temp){
            after = temp->next; 
            temp->next = before; 
            before = temp; 
            temp = after; 
        }


        ListNode* firstpart = head;
        slow->next = nullptr;  
        ListNode* reversed = before;  

        while(firstpart && reversed){
            ListNode* n = firstpart->next;
            ListNode* m = reversed->next; 

            firstpart->next = reversed; 
            reversed->next = n; 

            firstpart = n; 
            reversed = m; 
            
        }

        
    }
};
