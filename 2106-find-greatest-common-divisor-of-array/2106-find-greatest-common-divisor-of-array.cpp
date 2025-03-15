class Solution {
public:
    int findGCD(vector<int>& nums) {
        int max = nums[0];
        int min = nums[0];
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] > max){
                max = nums[i]; 
            }
            if (nums[i] < min) {
                min = nums[i];
            }
        }
        int divisor = 1;
        for (int i = 1; i <= min; i++){ 
            if (min % i == 0 && max % i == 0){
                divisor = i; 
            }
        }
        return divisor;
        return 0;}
};