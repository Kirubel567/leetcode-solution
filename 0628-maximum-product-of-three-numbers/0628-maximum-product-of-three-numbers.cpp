class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int product = 1; 
        int pos1, pos2; 
        int n = nums.size() - 1; 
        sort(nums.begin(), nums.end()); 
        pos1 = nums[n] * nums[n - 1] * nums[n -2]; 
        pos2 = nums[0] * nums[1] * nums[n]; 

        return max(pos1, pos2); 
        
    }
};