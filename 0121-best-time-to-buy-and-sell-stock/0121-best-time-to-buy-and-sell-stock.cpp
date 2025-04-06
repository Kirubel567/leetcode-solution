class Solution {
public:
    int maxProfit(vector<int>& prices) {
    //     int profit = 0; 
    //     for (int i = 0; i < prices.size(); i++){
    //         for (int j = i + 1; j < prices.size(); j++){
    //             if(prices[j] - prices[i] > profit){
    //                 profit = prices[j] - prices[i]; 
    //             }
    //         }
    //     }
    //     return profit; 
    int buy = prices[0]; 
    int profit = 0; 
    for (int i = 0; i < prices.size(); i++){
        if(prices[i] < buy){
            buy = prices[i]; 
        }else if(prices[i] - buy > profit){
            profit = prices[i] - buy; 
        }
    }
    return profit; 
    }

};