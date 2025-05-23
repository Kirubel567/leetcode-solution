class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int n = s.size(); 
        unordered_map<char, char> mapp(n); 
        unordered_map<char, char> map1(n); 

        for(int i = 0; i < n; i++){
            if(mapp.count(s[i]) && mapp[s[i]] != t[i]) return false; 
            mapp[s[i]] = t[i]; 
        }
        for(int i = 0; i < n; i++){
            if(map1.count(t[i]) && map1[t[i]] != s[i]) return false; 
            map1[t[i]] = s[i]; 
        }

        return true; 
        
    }
};