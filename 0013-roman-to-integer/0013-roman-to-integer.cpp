class Solution {
public:
    int romanToInt(string s) {
        int number = 0; 
        //if (int i != 4, 9, 40, 90, 400, 900){
            for (int j = 0; j < s.size();  j++){
                if (s[j] == 'I'){
                    if (s[j + 1] == 'V'){
                        number +=4; 
                        j++; 

                    }else if (s[j + 1] == 'X'){
                        number += 9; 
                        j++; 
                    }else {number += 1;} 
                }else if (s[j] == 'V'){
                    number += 5; 
                }else if (s[j] == 'X'){
                    if (s[j + 1] == 'L'){
                        number += 40; 
                        j++; 
                    }else if (s[j + 1] == 'C'){
                        number += 90;
                        j++;  

                    }else {number += 10; }
                }else if (s[j] == 'L'){
                    number += 50; 
                }else if (s[j] == 'C'){
                    if (s[j + 1] == 'D') {
                        number += 400; 
                        j++; 
                    }else if (s[j + 1] == 'M'){
                        number += 900;
                        j++;  
                    }else {number += 100; }
                }else if (s[j] == 'D'){
                    number += 500; 
                }else if (s[j] == 'M'){
                    number += 1000; 
                }
            }
    //}
      return number;
        }
        
        
    
};