class Solution {
public:
    string reverseVowels(string s) {
        int left = 0; 
        int right = s.size() - 1; 
        string check = "AEIOUaeiou"; 

        while (left <= right){
            
            if(check.find(s[right]) != string::npos && check.find(s[left]) != string::npos){
                int temp = s[right]; 
                s[right] = s[left]; 
                s[left] = temp;  
                right--; 
                left++; 
            }else if(check.find(s[left]) == string::npos){
                left++; 
            }else if (check.find(s[right]) == string::npos){
                right--; 
            }
        }
        return s; 
        
    }
};