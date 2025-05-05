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
    ListNode* reversed(ListNode* temp){
        ListNode* before = nullptr; 
        ListNode* after = temp; 
        while(temp){
            after = temp->next; 
            temp->next = before; 
            before = temp; 
            temp = after;  
        }
        return before; 
    }
public:
    ListNode* doubleIt(ListNode* head) {
        int sum = 0; 
        int carry =0;

        ListNode* dummy = new ListNode(); 
        ListNode* ans = dummy; 

        head = reversed(head); 
        

        while(head){
            sum = 2 * head->val + carry; 
            if(sum <= 9){
                ans->next = new ListNode(sum); 
                ans = ans->next; 
                carry = 0; 
            }else{
                sum = sum % 10;
                ans->next = new ListNode(sum); 
                ans = ans->next; 
                carry = 1; 
            } 
            head = head->next; 
        }
        if (carry > 0){
            ans->next = new ListNode(carry); 
        }

        return reversed(dummy->next); 
        
    }
};