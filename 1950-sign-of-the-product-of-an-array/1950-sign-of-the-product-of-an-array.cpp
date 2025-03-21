class Solution {
public:
    int signFunc(int product){
        if (product == abs(product)){
            if (product == 0){
                return 0; 
            }else{return 1;} 
        }else if (product != abs(product)){
            return -1; 
        }
        return 0; 
    }
    int arraySign(vector<int>& nums) {
        int Product = 1; 
        for (int i = 0; i < nums.size(); i++){
            Product *= signFunc(nums[i]); 
        }
        return signFunc(Product); 
    }
};