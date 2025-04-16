class Solution {
public:
    int minimumSum(int num) {
        // int Sum = 0; 
        // int num1, num2;
        // string numString1, numString2; 
        // int n1, n2;



        // string word = to_string(num); 
        // for (int i = 0; i < 2; i++){
        //     numString1 += word[i];
        // }
        // for(int i = 2; i < 4; i++){
        //     numString2 += word[i]; 
        // }

        // n1 = stoi(numString1); 
        // n2 = stoi(numString2); 

        // reverse(numString1.begin(), numString1.end()); 
        // if(stoi(numString1) < n1){n1 = stoi(numString1);}
        // reverse(numString2.begin(), numString2.end()); 
        // if(stoi(numString2) < n2){n2 = stoi(numString2); }


        // Sum = n1 + n2; 
        // return Sum; 

        int n1, num1, num2; 
        vector<int> nums; 

        while(true){
            n1 = num % 10;
            nums.push_back(n1); 
            num = num / 10;
             if(num == 0){
                break; 
            } 
        }

        sort(nums.begin(),  nums.end()); 

        num1 = nums[0] * 10 + nums[2]; 
        num2 = nums[1] * 10 + nums[3]; 

        return num1 + num2; 



        
    }
};