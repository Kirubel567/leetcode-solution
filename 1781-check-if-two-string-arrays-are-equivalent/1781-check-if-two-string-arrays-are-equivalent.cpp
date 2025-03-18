class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string one = ""; 
        for (int i = 0; i < word1.size(); i++){
            one += word1[i]; 
        }
        string two = ""; 
        for (int j = 0; j < word2.size(); j++){
            two += word2[j]; 
        }
        return one == two; 
        
    }
};