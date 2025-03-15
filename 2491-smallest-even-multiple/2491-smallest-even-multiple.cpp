class Solution {
public:
    int smallestEvenMultiple(int n) {
        if (n%2 != 0){
            return n *2;
        }
        else if (n%2 == 0){
            return n;
        }
        return 0;
    }
};