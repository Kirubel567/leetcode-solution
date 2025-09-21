class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n=coins.size();

        vector<int> dp(amount+1,INT_MAX);  dp[0]=0;
        vector<int> temp(amount+1,INT_MAX); temp[0]=0;

        for(int j=0;j<=amount;++j){
            if(j%coins[0]==0) dp[j]=j/coins[0];
        }

        for(int idx=1;idx<n;++idx){
            for(int sum=1;sum<=amount;++sum){
                long long notTake = dp[sum];
                long long take = INT_MAX;

                if(sum>=coins[idx]) take = 1ll + temp[sum-coins[idx]];
                temp[sum]=min(take,notTake);
            }
            dp=temp;
        }
        
        int sol = dp[amount];
        if(sol==INT_MAX) sol=-1;

        return sol;
    }
};