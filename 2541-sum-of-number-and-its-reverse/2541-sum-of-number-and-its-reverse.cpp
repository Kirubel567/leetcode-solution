class Solution {
public:
    bool sumOfNumberAndReverse(int num) {
        if(num == 0) return true; 
        for (int i = 0; i < num; i++){
            string rev = to_string(i); 
            reverse(rev.begin(), rev.end()); 
            int n = stoi(rev); 
            if(i + n == num) return true; 
        }

        return false; 
        
    }
};