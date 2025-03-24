class Solution {
public:
     string reverseOnlyLetters(string s) {
                int left = 0; 
                int right = s.size() - 1; 
                while (left < right){
                    if (isalpha(s[left])){
                         while (!isalpha(s[right])){
                            right--; 
                        }
                        if (isalpha(s[right])){
                            char temp = s[left];
                            s[left] = s[right]; 
                            s[right] = temp; 
                            left++; 
                            right--;}     
                    } else{
                        left++;  
                    }
                }
                return s; 
            }
};