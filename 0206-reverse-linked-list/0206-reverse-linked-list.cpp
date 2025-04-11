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
    ListNode* reverseList(ListNode* head) {
        ListNode* before = nullptr; 
        ListNode* temp = head;
        while(temp){
            ListNode* after = temp->next; 
            temp->next = before; 
            before = temp; 
            temp = after; 
        }
        return before;  
    }
    
};

// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         ListNode* prev = nullptr;
//         ListNode* curr = head;
//         while (curr != nullptr) {
//             ListNode* nextNode = curr->next; // save next
//             curr->next = prev;               // reverse link
//             prev = curr;                     // move prev
//             curr = nextNode;                 // move curr
//         }
//         return prev; // new head
//     }
// };