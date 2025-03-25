class Solution {
public:
    string finalString(string s) {
        // string Final = ""; 
        // string reversed = ""; 
        // for (char i : s){
        //     if (i == 'i'){
        //         for(int j = (Final.size() - 1); j >= 0; j--){
        //             reversed += s[j]; 
        //         }
        //         Final = reversed;
        //         }
        //     else {
        //         Final += i; 
        //     }
        //     }
        //     return Final; 
        string result = "";
        for (char c : s) {
            if (c == 'i') {
                reverse(result.begin(), result.end());
            } else {
                result += c;
            }
        }
        return result;
        }
        
    };
