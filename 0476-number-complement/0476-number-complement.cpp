class Solution {
public:
    int findComplement(int num) {
        int n;
        int result= 0;  
        vector<int> res; 

        while(num != 0){
            n = num % 2; 
            res.push_back(n);
            num = num / 2;   
        }

        for(int i = 0; i < res.size(); i++){
            if(res[i] == 1){
                res[i] = 0; 
            }else if(res[i] == 0){
                res[i] = 1; 
            } 
        }

        for(int i = res.size() - 1; i >= 0; i--){
            result += (pow(2, i) * res[i]); 
        }

        return result; 
        
    }
};