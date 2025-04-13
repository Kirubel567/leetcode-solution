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
    ListNode* removeNthFromEnd(ListNode* head, int n) { 
        ListNode* m = nullptr; 
        ListNode* temp = head; 
        ListNode* ptr1 = head; 
        ListNode* ptr2 = head; 
        
        if (head->next == nullptr) return m;
        if (head->next->next == nullptr){
            if(n == 2){
                head = head->next; 
                return head; 
            }
        }
        
        for(int i = 1; i < n; i++){
            ptr2 = ptr2->next; 
        }
        
        ptr2 = ptr2->next; 
        ptr1 = ptr1->next; 
        
        if (ptr2 != nullptr){
             while(ptr2->next){
            ptr2 = ptr2->next; 
            ptr1 = ptr1->next; 
            temp = temp->next;   
        }
        temp->next = temp->next->next;
        ptr1->next = nullptr; 
        delete ptr1; 
        }else {
            head = head->next; 
            return head; 
        }
        return head;
    }
};