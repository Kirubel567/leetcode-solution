// class Solution {
// public:
//     int addDigits(int num) {
//        int Sum = 10; 
//        while(Sum % 10 != Sum) {
//         int digit = num%10;
//         if (num == 0){
//         return 0;
//            }
//         Sum = digit + addDigits(num/10);
//         }
    
    
//     return Sum; }
// };

class Solution {
public:
    int addDigits(int num) {
        if (num == 0) return 0;
        if (num % 9 == 0) return 9;
        return num % 9;
    }
};