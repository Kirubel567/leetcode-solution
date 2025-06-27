class Solution {
public:
    int maxFreqSum(string s) {
        map<char, int> vowel; 
        map<char, int> consonant; 
        int vmax = 0, cmax = 0; 

        for(char c: s){
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                vowel[c]++; 
            }else{
                consonant[c]++; 
            }
        }

        for(auto [Consonant, freq] : consonant){
            if(freq > cmax){
                cmax = freq;
            }
        }
        for(auto [_, freq] : vowel){
            if(freq > vmax){
                vmax = freq; 
            }
        }

        return vmax + cmax; 
        
    }
};