class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size(); 
        int left = 2;

        for (int right = 2; right < nums.size(); right++){
            if (nums[right] != nums[left - 2]){
                nums[left] = nums[right]; 
                left++; 
            }

        } 
        return left; 

        
        
    }
};