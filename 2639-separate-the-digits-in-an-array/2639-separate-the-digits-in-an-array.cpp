class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> answer; 

        for (int num : nums){ 
            string numS = to_string(num); 
            for(int i = 0; i < numS.size(); i++){
                answer.push_back(numS[i] - '0'); 
            }
        }
        return answer; 
        
    }
};