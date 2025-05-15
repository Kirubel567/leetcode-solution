class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int Sum = nums[0];  
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == nums[i - 1] + 1){
                Sum += nums[i];  
            }else{
                break; 
            }
        }

  
        sort(nums.begin(), nums.end()); 
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == Sum) {
                Sum += 1; 
                }
        }
        
        return Sum;  
    }
};