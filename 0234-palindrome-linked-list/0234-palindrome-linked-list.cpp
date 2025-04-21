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
    bool isPalindrome(ListNode* head) {
        ListNode* lead = head; 
        ListNode* follow = head; 

        while(lead && lead->next){
            lead = lead->next->next;
            follow = follow->next;  
        }

        if(head == nullptr) return true; 
        ListNode* before = nullptr; 
        ListNode* temp = follow;
         
        while(temp){
            ListNode* after = temp->next; 
            temp->next = before; 
            before = temp; 
            temp = after; 
        }

        ListNode* check = head;
        while(before && check){
            if(before->val != check->val){
                return false; 
            }
            before = before->next; 
            check = check->next; 
        }

        return true;  
    }
};

