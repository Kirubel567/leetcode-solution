class Solution {
public:
    string removeStars(string s) {
        stack<char> remove;
        int count = 0;  
        

        for(int i = 0; i < s.size(); i++){
            if(s[i] == '*'){
                if(!remove.empty()){
                    remove.pop(); 
                } 
            }
            else{
                remove.push(s[i]);  
            }
        }


        string Final; 
        while(!remove.empty()){
            Final += remove.top(); 
            remove.pop(); 
        }


        string Finall; 
        for(int i = Final.size() - 1; i >= 0; i--){
            Finall += Final[i];  
        }

        return Finall; 
        
    }
};