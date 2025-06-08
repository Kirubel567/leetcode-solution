class Solution {
public:
    double myPow(double x, int n) {
       long long N = n; 
       if(N < 0){
        x = 1/x; 
        N = -N;
            }
       double half = pow(x, N/2); 
       if(N%2 == 0) return half * half; 
       return x * half * half; 
    }
};