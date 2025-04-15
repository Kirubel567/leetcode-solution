class Solution {
public:
    int countElements(vector<int>& nums) {
        // if (nums.size() <= 2) return 0; 
        // return nums.size() - 2;
        int count = 0; 
        int Max = nums[0]; 
        int Min = nums[0]; 
        for (int i = 1; i < nums.size(); i++){
            if(nums[i] < Min){ Min = nums[i]; }
            if(nums[i] > Max){Max = nums[i];}
        }
        for (int i = 0; i < nums.size(); i++){
            if(nums[i] != Min && nums[i] != Max){
                count++; 
            }
        }

        return count; 

        
    }
};