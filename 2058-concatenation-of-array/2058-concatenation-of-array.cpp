class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans; 

        for(int i = 0; i < 2 * nums.size(); i++){
            int m = i % nums.size(); 
            ans.push_back(nums[m]); 
        }

        return ans; 
        
    }
};