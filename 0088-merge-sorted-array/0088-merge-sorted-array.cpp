#include<algorithm> 
#include<functional>

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
       vector<int> merged; 

       for (int i = 0; i < m; i++){
        merged.push_back(nums1[i]);
       }
       
       for (int j = 0; j < n; j++){
        merged.push_back(nums2[j]);
       }
       sort(merged.begin(), merged.end()); 

       for(int i = 0; i < m + n; i++){
        nums1[i] = merged[i];
       }
    }
};