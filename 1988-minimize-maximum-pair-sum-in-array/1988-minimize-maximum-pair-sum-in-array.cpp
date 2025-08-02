class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 

        int start = 0; 
        int end = nums.size() - 1; 
        int Max = INT_MIN; 
        while(start < end){
            Max = max((nums[start] + nums[end]), Max); 
            end--; 
            start++; 
        }

        return Max; 
    }
};