class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int left = 0; 
        int right = n; 
        vector<int> result; 

        while(right < nums.size()){
            result.push_back(nums[left]); 
            result.push_back(nums[right]); 
            left++; 
            right++; 
        }
        return result; 
        
    }
};