class Solution {
public:
    bool equalFrequency(string word) {
        for(int i = 0; i < word.size();i++){
            unordered_map<char, int> mapp; 
            for(int j = 0; j < word.size(); j++){
                if(j != i) mapp[word[j]]++; 
            }
            int first_frequency = mapp.begin()->second; 
            bool ok = true; 
            for(auto i : mapp){
                if(i.second != first_frequency)  ok = false; 
            }
            if(ok) return true; 

        }
        return false; 
        
    }
};