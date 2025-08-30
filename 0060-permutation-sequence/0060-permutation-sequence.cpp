class Solution {
public:
    string getPermutation(int n, int k) {
        /*
            We will use the fact that we can find the value using mathematical
            computaion. By narrowing down the range for each position
        */

        vector<char> nums;
        int fact=1;

        for(int i=1;i<=n;++i){
            nums.push_back(i+'0');
            fact*=i;
        }
        
        k-=1; // Use 0 based indexing so the 0th would be the 1st
        string sol;

        while(!nums.empty()){
            fact/=nums.size();
            sol.push_back(nums[k/fact]);
            nums.erase(nums.begin()+k/fact);
            k%=fact;
        }

        return sol;
    }
};