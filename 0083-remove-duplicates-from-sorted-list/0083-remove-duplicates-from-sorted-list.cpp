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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp = head; 
        if(head == nullptr) return nullptr; 
        if (temp->next != nullptr){
              while (temp->next){
                if(temp->next->val == temp->val){
                ListNode* todelete = temp->next; 
                temp->next = todelete->next; 
                delete todelete; 
            }else{temp = temp->next; }
            
        }

        }
      
        return head; 
    }
};