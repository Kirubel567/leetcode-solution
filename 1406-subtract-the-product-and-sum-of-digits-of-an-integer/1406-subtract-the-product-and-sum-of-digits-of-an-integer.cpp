class Solution {
public:
    int Sum(int x){
        int digit = x % 10; 
        if(x == 0){
            return 0; 
        }
        int sum = digit + Sum(x / 10); 
        return sum; 
    }
    int Product(int x){
        int digit = x % 10; 
        if(x == 0){
            return 1; 
        }
        int product = digit * Product(x / 10);  
        return product; 
    }
    int subtractProductAndSum(int n) {

        return Product(n) - Sum(n); 
        
    }
};