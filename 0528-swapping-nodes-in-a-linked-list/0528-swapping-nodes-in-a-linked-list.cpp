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
    ListNode* swapNodes(ListNode* head, int k) {
        if(!head || !head->next) return head; // some edge cases

        ListNode* dummy = new ListNode(0, head);// I used this to get the node before the target nodes (the first and last kth node)
        
        ListNode* fast = dummy;
        ListNode* slow = dummy; 

        for(int i = 1; i < k; i++){// iterate through the linked list to get to target - 1 node
            fast = fast->next; 
        }
        ListNode* start = fast;// to know the place of the node before the kth node
        ListNode* target1 = start->next; // this is the first target to be swapped 
    
        fast = fast->next; // this is just used to get the node before the kth node from the last

        while(fast && fast->next){
            slow = slow->next; 
            fast = fast->next; 
        }

        // now we just need to swap, slow and start
        ListNode* target2 = slow->next;// to know the second tartget

        //if both targets are the same, no need to swap
        if(target1 == target2) return dummy->next; 
        
        if(target1->next == target2){
            start->next = target2; 
            target1->next = target2->next; 
            target2->next = target1; 
             
        }else if(target2->next == target1){
            slow->next = target1; 
            target2->next = target1->next; 
            target1->next = target2; 
        }

        else{ListNode* store = target1->next; 
        ListNode* store2 = target2->next;  

        start->next = target2; 
        slow->next = target1; 

        target2->next = store; 
        target1->next = store2; } 

        return dummy->next; 
    }
};