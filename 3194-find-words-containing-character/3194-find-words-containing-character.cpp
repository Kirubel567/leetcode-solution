class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> Final;

        for(int i = 0; i < words.size(); i++){
            if(words[i].find(x) != string::npos){
                Final.push_back(i); 
            }
        } 

        return Final; 
        
    }
};