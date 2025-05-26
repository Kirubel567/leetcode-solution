class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> map1; 
        unordered_map<string, char> map2;
        vector<string> vect; 
        string str1 = ""; 
        
        int i = 0; 
        while(i < s.size()){
            while(s[i] != ' ' && i < s.size()){
                    str1 += s[i]; 
                    i++; 
            }
            vect.push_back(str1); 
            str1 = ""; 
            i++; 
        }

        if(vect.size() != pattern.size()) return false;  
        for(int i = 0; i < pattern.size(); i++){
            if(map1.count(pattern[i]) && map1[pattern[i]] != vect[i]) return false; 
            if(map2.count(vect[i]) && map2[vect[i]] != pattern[i]) return false; 

            map2[vect[i]] = pattern[i]; 
            map1[pattern[i]] = vect[i]; 
        }
        return true; 
        
    }
};