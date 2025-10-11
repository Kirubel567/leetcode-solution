class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix_prod = 1; 
        int post_prod = 1; 
        vector<int> res(nums.size(), 1); 

        for(int i = 0; i < nums.size(); i++){
            res[i] *= prefix_prod; 
            prefix_prod *= nums[i]; 
        }

        for(int i = nums.size() -1; i > -1; i--){
            res[i] *= post_prod; 
            post_prod *= nums[i]; 
        }

        return res; 
    

    }
};
