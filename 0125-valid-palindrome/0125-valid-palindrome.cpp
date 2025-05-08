class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
        bool ans = true; 
        
        while(left < right){
            if(isalpha(s[right]) || isdigit(s[right])){
                if(isalpha(s[left]) || isdigit(s[left])){
                    if(tolower(s[right]) != tolower(s[left])) return !ans; 
                    else{
                        right--; 
                        left++;
                    }
                }
                else{
                    left++; 
                }
            }
            else{right--;} 
        }

        return ans; 
        
        
    }
};