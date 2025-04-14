class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        set<int> Set1(nums.begin(), nums.end());
        vector<int> numss(Set1.begin(), Set1.end()); 

        for(int num : numss){
            if(num != numss[numss.size() - 1] && num != numss[0]){
                    return num; 
                } 
        }
        return -1; 
    }
};