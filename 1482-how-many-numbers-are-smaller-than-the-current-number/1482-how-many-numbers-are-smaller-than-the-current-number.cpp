class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> Final; 
        int left = 0; 
        int right = 0;
        int count = 0; 

        while(right <= nums.size() && left < nums.size()){
            if(right == nums.size()){
                Final.push_back(count); 
                count = 0; 
                right = 0; 
                left++; 
                continue; 
            }
            if(right != left){
                if(nums[right] < nums[left]){
                    count++; 
                }
            }
            right++; 
        } 

        return Final; 

        
        
    }
};