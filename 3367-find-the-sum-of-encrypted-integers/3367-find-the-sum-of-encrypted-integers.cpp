class Solution {
public:
    int encrypt(int val){
        if(val == 0) return 0; 
        //count the number of digits to use it later to make the number all the same
        int count = 0; 
        //count the number of digits and find the maximum of all
        int dominate = -1; 
        while(val != 0){
            int digit = val % 10; 
            dominate = max(digit, dominate); 
            val /= 10; 
            count++; 
        }
        //now using count and the dominant create a number
        int encrypted = 0; 
        for(int i = 0; i < count; i++){
            encrypted = encrypted * 10 + dominate; 
        }
        return encrypted; 
    }
    int sumOfEncryptedInt(vector<int>& nums) {
        //now iterate through the array and add all the encrypted value of the elements
        int Sum = 0; 
        for(int i = 0; i < nums.size(); i++){
            Sum += encrypt(nums[i]); 
        }

        return Sum; 
        
    }
};