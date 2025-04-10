class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0; 
        int right = numbers.size() - 1; 
        vector<int> Final; 

        while (left <= right){
            if (numbers[right] + numbers[left] < target){
                left++; 
            }
            else if (numbers[right] + numbers[left] > target){
                right--; 
            }
            else if (numbers[right] + numbers[left] == target){
                Final.push_back(left + 1); 
                Final.push_back(right + 1);
                break; 
            }
        }
        return Final; 
       
        
    }
};