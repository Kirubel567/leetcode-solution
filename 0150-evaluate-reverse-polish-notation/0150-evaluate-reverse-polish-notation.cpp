class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long> st;
        long first, second, Sum, diff, product, div; 

        for(string c: tokens){
            if(c != "+" && c != "-" && c != "*" && c != "/"){
                st.push(stoi(c));
            }else{
                second = st.top(); 
                st.pop(); 
                first = st.top(); 
                st.pop();
                Sum = first + second; 
                diff = first - second; 
                product = first * second; 
                if(second != 0)div = first / second; 
                if(c == "+") st.push(Sum); 
                else if(c == "-") st.push(diff); 
                else if(c == "*") st.push(product); 
                else st.push(div); 
                Sum = 0; diff = 0; product = 0; div = 0; 
            }
        }

        return st.top(); 
        
    }
};