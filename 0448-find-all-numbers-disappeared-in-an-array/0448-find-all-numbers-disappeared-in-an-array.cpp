class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_map<int, bool> seen; 
        vector<int> res; 
        for(int num : nums){
            seen[num] = true; 
        }

        for(int i = 1; i <= nums.size(); ++i){
            if(!seen[i]){
                res.push_back(i); 
            }
        }

        return res; 
        // int length = nums.size(); 
        // set<int> Set(nums.begin(), nums.end()); 
        // vector<int> Res(Set.begin(), Set.end());
        // vector<int> Result; 
         

        // for (int i = 1; i <= Res.size(); i++){
        //     if(Res[i - 1] != i){
        //         Result.push_back(i); 
        //     }
        // } 
        // if(length == 2) {Result.push_back(2);} 
        // return Result; 
    }
};