class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;

        int Max = candies[0]; 
        for(int i = 1; i < candies.size(); i++){
            if(candies[i] > Max){
                Max = candies[i]; 
            }
        }

        for(int i = 0; i < candies.size(); i++){
            if(extraCandies + candies[i] >= Max){
                result.push_back(true); 
            }else{
                result.push_back(false); 
            }
        }

        return result; 
        
    }
};