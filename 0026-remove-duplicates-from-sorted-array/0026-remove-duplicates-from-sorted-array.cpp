class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 0; 
        int right = 1; 

        while (right < nums.size()){
            if (nums[right] != nums[left]){
                left++; 
                nums[left] = nums[right]; 
               
            }
             right++; 
        }
        return left + 1; 
    }
};