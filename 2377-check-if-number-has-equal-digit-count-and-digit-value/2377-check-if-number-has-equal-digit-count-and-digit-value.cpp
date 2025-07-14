class Solution {
public:
    bool digitCount(string num) {
        map<int, int> freq; 
        for(char c : num){
            freq[c - '0']++; 
        }
        bool check = true; 
        for(int i = 0; i < num.size(); i ++){
            if(freq[i] != num[i] - '0'){
                check = false; 
                break;
            }
        }
        if(check){
            return true;
        }
        return false; 

    }
};