class Solution {
public:
    int strStr(string haystack, string needle) {
         haystack.find(needle); 
         if (haystack.find(needle) != string::npos){
            return haystack.find(needle);
         } 
         return -1;
        
    }
};