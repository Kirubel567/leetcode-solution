class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int n=nums.size();
        unordered_map<int, int> mp;
        int zeros=0, nonzeros=0;
        if(n==1){
            if(nums[0]==0) return 0;
            else return 1;
        }
        for(int i=0; i<n; i++){
            if(nums[i]==0) zeros++;
            mp[nums[i]]++;
        }
        if(zeros){
            return mp.size()-1;
        }
        return mp.size();
    }
};