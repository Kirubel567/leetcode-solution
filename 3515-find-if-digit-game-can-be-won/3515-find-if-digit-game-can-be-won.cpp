class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int Sum = 0; 
        int Sum2 = 0; 
        for (int num : nums){
            if (to_string(num).size() == 1){
                Sum += num; 
            }if(to_string(num).size() == 2){
                Sum2 += num; 
            }
        }
        return Sum2 != Sum; 
        
        
    }
};