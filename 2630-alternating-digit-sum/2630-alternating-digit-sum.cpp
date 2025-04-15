class Solution {
public:
    int alternateDigitSum(int n) {
        int Sum = 0; 
        int m = 1; 
        int y = -1;

        string word = to_string(n); 
        for(int i = 0; i < word.size(); i++){ 
            if(i % 2 == 0){
                Sum += (word[i] - '0') * m; 
            }else{Sum += (word[i] - '0') * y;}  
        }
        
        return Sum; 
        
    }
};