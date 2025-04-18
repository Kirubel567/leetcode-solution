class Solution {
public:
    int minimumSum(int num) {
           int n1, num1, num2; 
        vector<int> nums; 

        while(true){
            n1 = num % 10;
            nums.push_back(n1); 
            num = num / 10;
             if(num == 0){
                break; 
            } 
        }

        sort(nums.begin(),  nums.end()); 

        num1 = nums[0] * 10 + nums[2]; 
        num2 = nums[1] * 10 + nums[3]; 

        return num1 + num2;    
        
    }
};