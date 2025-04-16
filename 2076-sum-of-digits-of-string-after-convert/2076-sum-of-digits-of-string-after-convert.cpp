class Solution {
public:

    int sum(int num){
        int digit = num % 10; 
        if(num == 0){
            return 0; 
        }
        int Sum = digit + sum(num / 10); 
        return Sum; 
    }
    int getLucky(string s, int k) {
        int num = 0; 
        string newNum; 
        map<char, int> alphabetNum = {{'a', 1}, {'b', 2}, {'c', 3}, {'d', 4},
        {'e', 5},{'f', 6}, {'g', 7}, {'h', 8}, {'i', 9}, {'j', 10}, {'k', 11},
        {'l', 12}, {'m', 13}, {'n', 14}, {'o', 15}, {'p', 16}, {'q', 17}, 
        {'r',18}, {'s', 19}, {'t', 20}, {'u', 21}, {'v', 22}, {'w', 23}, 
        {'x', 24}, {'y', 25}, {'z', 26}}; 


        for(char n : s){
            newNum += to_string(alphabetNum[n]); 
        }

        for(char n : newNum){
              num += n - '0'; 
        }
    

        for(int i = 0; i < k - 1; i++){
            num = sum(num); 
        }



        return num;        
    }
};


