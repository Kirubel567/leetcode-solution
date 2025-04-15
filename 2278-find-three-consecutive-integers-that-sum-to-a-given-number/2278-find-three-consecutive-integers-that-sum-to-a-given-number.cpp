class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        vector<long long> res; 

        long long x = num / 3;
        if((x-1) + (x) + (x + 1) == num){
            res.push_back(x -1); 
            res.push_back(x);
            res.push_back(x + 1);
            return res; 
        }


        return res; 
        
    }
};