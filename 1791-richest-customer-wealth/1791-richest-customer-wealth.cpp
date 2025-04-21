class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int Sum = 0; 
        int output = 0; 
        for(int i = 0; i < accounts.size(); i++){
            Sum = 0; 
            for(int j = 0; j < accounts[0].size(); j++){
                Sum += accounts[i][j]; 
                output = max(output, Sum); 
            }
        }

        return output; 
        
    }
};