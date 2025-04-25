class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end()); 
        
        int count = 0; 
        int left = 0; 
        int right = people.size() - 1; 

        while(left <= right){
            if(people[right] + people[left] <= limit){
                count++; 
                right--; 
                left++; 
            }else{
                right--; 
                count++; 
            }
        }
        return count; 
        
    }
};