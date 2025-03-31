class Solution {
public:
    bool isPowerOfFour(int n) {
         for (int m = 0; pow(4, m) <= n; m++){
            if (n == pow(4, m)){
            return true; 
            break; 
        }
        }
        return false; 
        
    }
};