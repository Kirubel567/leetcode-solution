class Solution {
public:
    bool symmetric(int n){
        int half_one = 0; 
        int half_two = 0; 

        int m = n; 
        //first count if the number of digits is even or odd 
        int count = 0; 
        while(n != 0){
            n /= 10; 
            count++; 
        }
        // if odd just return false
        if(count % 2 != 0){
            return false; 
        }
        // if even check the sum of the two halfs
        else{
            for(int i = 0; i < count/2; i++){ //add the last half digits
                half_one = half_one + (m % 10); 
                m = m/10; 
            } 
            for(int j = 0; j < count/2; j++){//add the first half digits
                half_two = half_two + (m % 10); 
                m = m/10;  
            }
            if(half_one == half_two) return true; //compare and return
        }
        return false;
    }

    int countSymmetricIntegers(int low, int high) {
        int counter = 0; 
        for(int i = low; i <= high; i++){//start from low and go to high 
            if(symmetric(i)){
                counter++; 
            }
        }

        return counter; 
        
    }
};