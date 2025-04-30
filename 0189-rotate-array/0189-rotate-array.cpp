class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size(); 
        vector<int> inter; 
        
        for(int i = nums.size() - k; i < nums.size(); i++){
            inter.push_back(nums[i]); 
        }
        for(int i = 0; i < nums.size() - k; i++){
            inter.push_back(nums[i]); 
        }
        for(int i = 0; i < nums.size(); i++){
            nums[i] = inter[i]; 
        }

        
        

        
    }
};