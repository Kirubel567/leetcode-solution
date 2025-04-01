class Solution {
public:
    bool isValid(string s) {
        stack<int> para; 

        for (char i : s){
            if (i == '{'){
                para.push('{'); 
            }else if (i == '('){
                para.push('('); 
            }else if(i == '['){
                para.push('['); 
            }else if (i == '}'){
                if (!para.empty()){
                    if(para.top() == '{'){
                    para.pop(); 
                } else { para.push('}');}
                }else { para.push('}');}
            }else if (i == ')'){
                if (!para.empty()){
                    if(para.top() == '('){
                    para.pop(); 
                } else { para.push(')');} 
                }else { para.push(')');} 
            }else if(i == ']'){
                if (!para.empty()){
                    if(para.top() == '['){
                    para.pop(); 
                } else { para.push(']');}

                }else { para.push(']');} 
            }
        } 
        if (para.empty()){
            return true; 
        }
        return false;   
    }
};