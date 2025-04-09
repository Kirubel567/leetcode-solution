class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int Sum = 0; 
        int outPut = nums[0]; 
        for (int i = 0; i < nums.size(); i++){
            if (Sum < 0){
                Sum = 0; 
            }
            Sum += nums[i]; 
            outPut = max(outPut, Sum );
        }
        return outPut; 
        
    }
};