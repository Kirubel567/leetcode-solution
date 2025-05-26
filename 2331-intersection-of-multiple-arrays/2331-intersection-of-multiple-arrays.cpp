class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        unordered_map<int, int> mapp; 
        unordered_map<int, int> compare; 
        vector<int> vect; 


        for(int i = 0; i < nums[0].size(); i++){
            compare[nums[0][i]]++; 
        }
        

        for(int i = 1; i < nums.size(); i++){ 
            for(int j = 0; j < nums[i].size(); j++){
                if(compare.count(nums[i][j])){
                    mapp[nums[i][j]]++; 
                }
            }
            compare = mapp;
            mapp.clear(); 
        }

        for(auto& c: compare){
            vect.push_back(c.first); 
        }
        sort(vect.begin(), vect.end());
        return vect; 
    }
};