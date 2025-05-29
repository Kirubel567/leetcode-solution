class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        string intermediate, result, Fresult; 

        for(char& c : s){
            c = toupper(c); 
        } 

        for(int i = s.size() - 1; i >= 0; i--){
            if(s[i] != '-') intermediate += s[i];  
        }

        int n = 1; 
        for(int i = 0; i < intermediate.size(); i++){
            if(i == n * k - 1){
                result += intermediate[i]; 
                n++; 
                if(i != intermediate.size() - 1) result += '-'; 
            }else result += intermediate[i]; 
        }

        reverse(result.begin(), result.end()); 

       return result;   
    }
};