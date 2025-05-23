#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return 0;
        
        vector<int> prefix_max(n);
        vector<int> suffix_max(n);
        
        prefix_max[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            prefix_max[i] = max(prefix_max[i-1], nums[i]);
        }
        
        suffix_max[n-1] = nums[n-1];
        for (int i = n-2; i >= 0; --i) {
            suffix_max[i] = max(suffix_max[i+1], nums[i]);
        }
        
        long long max_val = 0;
        for (int j = 1; j < n - 1; ++j) {
            long long diff = prefix_max[j-1] - nums[j];
            if (diff <= 0) continue;
            long long current = diff * suffix_max[j+1];
            if (current > max_val) {
                max_val = current;
            }
        }
        
        return max_val;
    }
};