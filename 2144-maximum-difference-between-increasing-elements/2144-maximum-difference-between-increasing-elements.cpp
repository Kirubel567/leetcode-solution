class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int start = nums[0]; 
        int diff = 0; 
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] < start){
                start = nums[i]; 
            }
            else if (nums[i] - start > diff){
                diff =  nums[i] - start;  
            }
        }
        if (diff > 0) {
            return diff; 
        }else{return -1; }
        
    }
};