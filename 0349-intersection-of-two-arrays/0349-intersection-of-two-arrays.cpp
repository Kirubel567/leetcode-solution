class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // vector<int> intersect; 
        // unordered_set<int> Final; 
         
        // for(int i = 0; i < nums1.size(); i ++){
        //     for(int j = 0; j < nums2.size(); j++){
        //         if (nums1[i] == nums2[j]){
        //             Final.insert(nums1[i]); 
        //         }
        //     }
        // }
        // vector<int> Final_vector(Final.begin(), Final.end());
        
        // return Final_vector; 

        unordered_set<int> set(nums1.begin(), nums1.end()); 
        unordered_set<int> store; 

        for(int num : nums2){
            if(set.count(num)){
                store.insert(num); 
            }
        }
        vector<int> Final(store.begin(), store.end()); 
        return Final; 
        
    }
};