class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> result;
        for (int i = 0; i < words.size(); i++){
            for(int j =  0; j < words.size(); j++){
                if(words[i].find(words[j]) != string::npos){
                    if(words[i] != words[j]){
                        result.push_back(words[j]);
                    }
                     
                }

            }
        }
        unordered_set<string> Set(result.begin(), result.end()); 
        vector<string> Print(Set.begin(), Set.end()); 
        return Print; 
        
    }
};