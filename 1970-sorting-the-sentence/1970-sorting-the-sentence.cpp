class Solution {
public:
    string sortSentence(string s) {
        string ans;
        vector<string> temp(10);  // indices 1 to 9 used

        string word;
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                temp[s[i] - '0'] = word + " ";
                word = "";
                i++;  // skip the digit
            } else {
                word += s[i];
            }
        }

        for (auto& str : temp) {
            ans += str;
        }

        ans.pop_back();  // remove trailing space
        return ans;
    }
};