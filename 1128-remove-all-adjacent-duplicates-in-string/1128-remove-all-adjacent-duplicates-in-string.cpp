class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> st; 
        string str, str2; 

        for(int i = 0; i < s.size(); i++){
            if(!st.empty() && st.top() == s[i]) st.pop(); 
            else st.push(s[i]); 
        }

        while(!st.empty()){
            char c = st.top(); 
            st.pop(); 
            str += c; 
        }

        for(int i = str.size() - 1; i >= 0; i--){
            str2 += str[i]; 
        }

        return str2; 

        
        
    }
};