class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> res; 
        for (int i = 0; i < digits.size(); i++){
            for(int j = 0; j < digits.size(); j++){
                if(i == j) continue; 
                for(int l = 0; l < digits.size(); l++){
                    if(j == l || l == i) continue; 
                    int num = (digits[i] * 100) + (digits[j] * 10) + (digits[l]); 
                    if(num >= 100 && num % 2 == 0) {
                        res.push_back(num); 
                    }
                }
            }
        }
        set<int> Set(res.begin(), res.end()); 
        vector<int> Final(Set.begin(), Set.end()); 
        return Final; 
        
    }
};