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
    ListNode* deleteMiddle(ListNode* head) {
        if(head->next == nullptr || head == nullptr) {
            head = nullptr; 
            return head; 
        }
        ListNode* dummy = new ListNode(0, head); 
        ListNode* temp = dummy;
        ListNode* temp1 = head; 
        int count = 1; 


        while(temp1->next){
            temp1= temp1->next; 
            count++; 
        } 


        for(int i = 0; i < count / 2; i++){
            temp = temp->next; 
        }


        ListNode* toDelete = temp->next; 
        temp->next = toDelete->next; 
        delete toDelete; 

        head = dummy->next; 
        delete dummy; 
        return head;    
    }
};