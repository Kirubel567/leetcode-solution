class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> compare1; 
        stack<char> compare2; 

        for(char c : s){
            if( c == '#'){
                if(!compare1.empty()){
                    compare1.pop(); 
                }}
                else{
                    compare1.push(c); 
                } 
            
        }
         for(char c : t){
            if( c == '#'){
                if(!compare2.empty()){
                    compare2.pop(); 
                }}
                else{
                    compare2.push(c); 
                } 
            
        }

        return compare1 == compare2; 
        
    }
};