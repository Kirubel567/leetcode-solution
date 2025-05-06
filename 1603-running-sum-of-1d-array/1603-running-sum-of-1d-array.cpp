class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int accumulator= 0; 
        for(int i = 0; i < nums.size(); i ++){
            accumulator += nums[i]; 
            nums[i] = accumulator; 
        }

        return nums; 
        
    }
};