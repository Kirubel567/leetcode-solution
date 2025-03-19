class Solution {
public:
    unordered_map<int, int> memo; // Cache results across recursive calls

    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        if (memo.find(n) != memo.end()) return memo[n]; // Check cache

        return memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);
    }

    int main(int n) {
        return tribonacci(n);
    }
};