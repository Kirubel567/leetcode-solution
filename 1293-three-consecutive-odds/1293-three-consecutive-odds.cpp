class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        if(arr.size() < 3) return false; 
        bool test = false; 
        for(int i = 0; i < arr.size()-2; i++){
            if(arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0){
                test = true; 
                return test;
            }
        }
        if(!test){
            if(arr[arr.size() - 3] % 2 != 0 && arr[arr.size()- 2] % 2 != 0 && arr[arr.size() - 1] % 2 != 0){
                test = true; 
                return test; 
            }
        }

       
        

        
    return false;}
}; 