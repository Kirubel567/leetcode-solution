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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !head->next || k == 0) return head; 
        vector<ListNode*> nums;//to store the nodes of the linked list
        vector<ListNode*> inter;//to reverse the linked list 
        int count = 0; // to find the length of the linked list
        ListNode* temp = head;
        while(temp){
            nums.push_back(temp);
            temp = temp->next; 
        }
        count = nums.size(); 
        k = k % count;// to accomodate for k values that are greater the size of the linked list
        if(k == 0) return head; 
       

        ListNode* Temp = nums[count - k];//mapping the start of the reverse
        nums[count - k - 1]->next = nullptr; 
        for(int i = count - k; i < count; i++){//to find the node before the target, as when we move the target to the first index we need this node to make this node's next to null
            inter.push_back(nums[i]);//adding the last k elements to the vector first 
        } 

        for(int i = 0; i < count - k; i++){
            inter.push_back(nums[i]);// then adding the first elements...  
        }

        inter[k - 1]->next = head;// connecting the last element of inter to the first element of the linked list  

        return Temp; 
        
        

        

        
    }
};