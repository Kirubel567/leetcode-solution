class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res; 
        unordered_map<int, int> mapp; 
        int m = nums.size()/ 3;

        for(int n : nums){
            mapp[n]++; 
        } 

        for(auto c : mapp){
            if(c.second > m){
                res.push_back(c.first); 
            }
        }

        return res; 
        
    }
};