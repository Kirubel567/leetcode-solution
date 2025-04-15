class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int x = 0; 
        int y = 0; 
        for (int num : nums){
            string word = to_string(num); 
            for(int i = 0; i < word.size(); i++){
                y += (word[i] - '0'); 
            }
            x += num; 
        }

        return abs(y - x); 
        
    }
};