class Solution {
public:
    int sum(int n){
        int digit = n % 10; 
        if (n == 0){
            return 0;
        }
        n /= 10; 
        int Sum = digit + sum(n); 
        return Sum; 
    }
    int countEven(int num) {
        int count = 0;
        for (int i = 1; i <= num; i++){
            if (sum(i) % 2 == 0){
                count++; 
            }

            
        }
    return count; 
    }
};