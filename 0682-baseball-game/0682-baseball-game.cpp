class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> Final; 

        for (int i = 0; i < operations.size(); i++){
            if (operations[i] == "+"){
                int n = Final.top(); 
                Final.pop(); 
                int m = Final.top();
                Final.push(n); 
                Final.push(m + n);  
            }else if (operations[i] == "D"){
                Final.push(2 * Final.top()); 
            }else if (operations[i] == "C"){
                Final.pop(); 
            }else {
                int num = stoi(operations[i]); 
                Final.push(num); 
            }
        }
        int Sum = 0; 
        while (!Final.empty()){
            Sum += Final.top(); 
            Final.pop();
        }
        return Sum;  
        }
        
    };
