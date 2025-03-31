class Solution {
public:
    bool isPowerOfThree(int n) {
        for (int m = 0; pow(3, m) <= n; m++){
            if (n == pow(3, m)){
            return true; 
            break; 
        }
        }
        return false; 
        
    }
};