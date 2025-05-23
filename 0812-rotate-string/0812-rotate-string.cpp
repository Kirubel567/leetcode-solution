class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s == goal) return true; 
        int n = s.size(); 
        string sub = s;
        
        for(int i = 1; i < s.size(); i++){
            sub = sub.substr(1, n); 
            sub+= s[i - 1]; 
            if(sub == goal) return true; 
        }

        return false; 

        
        
    }
};