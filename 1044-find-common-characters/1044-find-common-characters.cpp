class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        unordered_map<char, int> base, counter; 
        vector<string> Final; 
        for(char c: words[0]){
                base[c]++; 
            }

        for(int i = 1; i< words.size(); i++){
            for(char c: words[i]){
                if(base.count(c) && base[c] > counter[c]){
                    counter[c]++; 
                }
            }
            base = counter; 
            counter.clear(); 
        }

        for(auto& c : base){
            for(int j = 0; j < c.second; j++){
                Final.push_back(string(1, c.first)); 
            }
        }

        return Final; 
        
    }
};