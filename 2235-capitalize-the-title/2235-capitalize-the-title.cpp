class Solution {
public:
    string capitalizeTitle(string title) {
        int len = 0; 
        

        for(int i = 0; i < title.size(); ){
            int j = i; 
            while(j < title.size() && title[j] != ' '){
                j++; 
            }

            len = j - i; 
            if(len <= 2){
                title[i] = tolower(title[i]); 
            }else{
                title[i] = toupper(title[i]); 
            }

            for(int k= i + 1; k < j; k++){
                title[k] = tolower(title[k]); 
            }

            i = j + 1; 
        }
        return title; 
        
    }
};