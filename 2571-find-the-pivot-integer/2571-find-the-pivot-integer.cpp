class Solution {
public:
    int pivotInteger(int n) {
        for(int i = 1; i <= n; i++){
            int sum1 = 0; 
            for(int j = 1; j <= i; j++){
                sum1 += j; 
            }
            int sum2 = 0; 
            for(int k = i; k <= n; k++){
                sum2 += k; 
            }
            if(sum1 == sum2){
                return i; 
            }
        }

        return -1; 
        
    }
};