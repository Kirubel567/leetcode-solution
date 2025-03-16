class Solution {
public:
    string interpret(string command) {
        string parsed = "";
        for(int i=0; i < command.size(); i++ ){
            if (command[i]  == 'G'){
                parsed += 'G';
            }else if (command[i] == '('){
                if (command[i+1] == ')'){
                    parsed += 'o';
                    i++;
                }
            }else{
                parsed += "al";
                i += 2;
            }
        }
        return parsed;
    }
};