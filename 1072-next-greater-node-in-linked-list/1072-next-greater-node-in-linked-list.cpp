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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> arr; 
        ListNode* temp = head; 
        int count = 0; 

        while(temp){
            count++; 
            temp = temp->next; 
        }
        ListNode* another = head; 
        for(int i = 0; i < count; i++){
            arr.push_back(another->val); 
            another = another->next; 
        }
        
        for(int i = 0; i < arr.size(); i++){
            bool test = true;
            for(int j = i + 1; j < arr.size(); j++){
                if(arr[i] < arr[j]){
                    arr[i] = arr[j]; 
                    test = false; 
                    break; 
                }
            }
            if (test){
                arr[i] = 0; 
            }  
        }

        return arr; 
        
        
    }
};