class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        vector<double> answer; 
        int left = 0; int right = nums.size() - 1; 
        sort(nums.begin(), nums.end()); 
        while (left < right){
            answer.push_back((nums[left] + nums[right])/2.0); 
            left++; 
            right--; 
        }
        double MIN = answer[0]; 
        for(int i = 1;i < answer.size(); i++){
            if(MIN > answer[i]){
                MIN = answer[i]; 
            }
        } 
        return MIN;  
    }
};