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
    int GCF(int a, int b){
        return b == 0 ? a : gcd(b, a%b); 
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {

        if(!head || !head->next) return head; 
        ListNode* ptr1 = head; 
        ListNode* ptr2 = head->next; 

        while(ptr2){
            ListNode* Value = new ListNode(GCF(ptr1->val, ptr2->val), ptr2); 
            ptr1->next = Value; 

            ptr1 = ptr2; 
            ptr2 = ptr2->next; 
        }

        return head;    
    }
};