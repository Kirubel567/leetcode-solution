class Solution {
public:
    int sum(int n){
        int digit = n % 10; 
        if(n == 0){
            return 0; 
        }
        int Sum = digit + sum(n/10); 
        return Sum; 
    }
    int minElement(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            nums[i] = sum(nums[i]); 
        }
        int Min = nums[0]; 
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] < Min){Min = nums[i];}
        }
        return Min; 
        
    }
};