class Solution {
public:
    bool canAliceWin(int n) {
        int i = 10; 
        while(n >= 0){
            if(n - i < 0 && i % 2 == 0) return false; 
            n = n - i; 
            i--; 
        }
        return true; 
        
    }
};