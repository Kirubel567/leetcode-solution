class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> Final; 
        int n = p.size(); 
        unordered_map<char, int> compare(p.size()), target(p.size()); 
      
        

        for(int i = 0; i < n; i++){
            target[p[i]]++; 
        }

        int i = 0; 
        while(n <= s.size()){
            for(int j = i ; j < n; j++){
            compare[s[j]]++;
            }
             
            if(compare == target){
                Final.push_back(i); 
            }
            
            i++;
            n++; 
            compare.clear(); 
        }
        
        return Final;} 
};