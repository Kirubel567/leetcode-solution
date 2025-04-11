class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.size();  
        int n2 = word2.size(); 
        string added = ""; 
        for(int i = 0, j = 0; i < min(n1, n2); i++, j++){
            added += word1[i]; 
            added += word2[j];
        }
        if (n1 > n2){
            string toAppend = word1.substr(n2); 
            added.append(toAppend); 
        }else if (n2 > n1){
             string toAppend = word2.substr(n1); 
             added.append(toAppend); 
        }
     return added;    
    }
};


