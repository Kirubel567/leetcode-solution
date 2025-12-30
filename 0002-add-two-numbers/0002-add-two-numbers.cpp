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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode(); 
        ListNode* track = ans; 

        int sum = 0; 
        int carry = 0;
        int val1 = 0,  val2 = 0;  

        while(l1 != nullptr || l2 != nullptr){
            if(l1 == nullptr){
                val1 = 0; 
            }else{val1 = l1->val;}
        
            if(l2 == nullptr){
                val2 = 0; 
            }else{val2 = l2->val; }

            sum = val1 + val2 + carry;
            

            if(sum <= 9){
                track->next = new ListNode(sum); 
                track = track->next;  
                carry = 0; 
            }else{
                sum = sum % 10; 
                track->next = new ListNode(sum); 
                track = track->next; 
                carry = 1; 
            }
            
            if(l1) l1 = l1->next; 
            if(l2) l2 = l2->next; 
            
        }
        if(carry > 0){
                track->next = new ListNode(carry); 
            }
        return ans->next; 
    
       

        
    }
};
