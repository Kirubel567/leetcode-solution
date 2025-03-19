class Solution {
public:
       unordered_map<int, int> memo;
    int climbStairs(int n) {
        if (n <= 3)
            return n; 
        if (memo.find(n) != memo.end()) return memo[n];
        return memo[n] = climbStairs(n -1) + climbStairs(n -2); // this is just to avoid the time limit exeeded error     
    }
    int main(int n){
        return climbStairs(n);
    }
};