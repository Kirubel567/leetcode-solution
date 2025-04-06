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
     int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice)
                minPrice = price;
            else
                maxProfit = max(maxProfit, price - minPrice);
        }

        return maxProfit;    
    }

};