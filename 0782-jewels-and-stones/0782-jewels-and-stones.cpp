class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> store; 

        for(char c: jewels){
            store[c]++; 
        }
        int count = 0; 
        for(char i : stones){
            if(store.count(i)){
                count ++; 
            }
        }

        return count; 
        
    }
};