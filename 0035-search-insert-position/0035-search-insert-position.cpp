
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
//use binary search for this problem, start with two pointers then serch through the array
        int start = 0; 
        int end = nums.size() - 1; 
        while (start <= end){
            int middle = (start + end)/2; 
            if (target == nums[middle]){
                return middle; 
            }if (target < nums[middle]){
                end = middle - 1; 
            }if (target > nums[middle]){
                start = middle + 1; 
            }
            
        }
        return start; }
        };
       
     
    
