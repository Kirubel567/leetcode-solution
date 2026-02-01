class Solution {
public:
    bool isPowerOfTwo(int n) { 
        for (int m = 0; pow(2, m) <= n; m++){
            if (n == pow(2, m)){
            return true; 
            break;   
        }
        }
        return false; 
        
    }
};
