class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int count = 0;

        for(string str : operations){
            if(str == "++X" || str == "X++"){
                count++; 
            }else{
                count--; 
            }
        } 

        return count; 

        
        
    }
};