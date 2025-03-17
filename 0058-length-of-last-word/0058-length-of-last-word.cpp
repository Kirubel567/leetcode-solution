class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = (s.size() - 1); 
        while (i >= 0 && s[i] == ' '){
            i--;
        }
        auto m = i; 

        while (m>=0 && s[m] != ' '){
            m--;

        }

        return i - m; 
        /*for (char i = (s.size() - 1); i >= Diff ; i--){
            if (s[i] == ' '){
                null += ' ';
                continue;
            }
            if (s[i] != ' '){
                 continue;
            }
            int Diff = start - i; 
            int diff = Diff - null;
            break;
        }
        return LastWord.size(); */   
   }
};