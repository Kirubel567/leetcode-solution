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
    ListNode* swapPairs(ListNode* head) {
        if(!head || !head->next) return head; 

        vector<ListNode*> result; 
        ListNode* temp = head; 

        while(temp){
            result.push_back(temp); 
            temp = temp->next; 
        }
        
        ListNode* connect = nullptr;  
        for(int i = 0; i < result.size()-1; i+=2){
            ListNode* save = result[i + 1]->next; 

            result[i + 1]->next = result[i];
            result[i]->next = save;

            if(connect){
                connect->next = result[i + 1]; 
            }

            connect = result[i]; 

            


             
            
           
            if(i == 0){
                head = result[i + 1]; 
            }
        }

        return head; 
        
    }
};