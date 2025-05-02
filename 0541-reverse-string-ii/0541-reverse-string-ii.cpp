class Solution {
public:
    string reverseStr(string s, int k) {
        for(int i = 0; i < s.size(); i += 2 * k){
            int left = i; 
            int right = min((int)s.size() - 1, i + k - 1); 

        while (left < right){
            swap(s[left], s[right]); 
            left++; 
            right--; 
        }

        }
        

        return s; 
        
    }
};