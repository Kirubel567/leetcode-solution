class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int Sum = 0;
        int Start = 0; 
        double average = 0;   
        for(int i = 0; i < k; i++){
            Sum += nums[i];
        }

         average = (double) Sum/k; 

        for(int i = k; i < nums.size(); i++){
            Sum += nums[i] - nums[i - k];  
            double average2 = (double)Sum /k; 

            if(average2 > average){
                average = average2; 
            }
            

            
        }

        return average; 
        
    }
};