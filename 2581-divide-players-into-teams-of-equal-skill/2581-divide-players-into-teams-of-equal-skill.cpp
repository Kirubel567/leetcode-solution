class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int left = 0; 
        int right = skill.size() - 1;
        long long chem = 0;  
        sort(skill.begin(), skill.end()); 

        int Sum = skill[right] + skill[left]; 

        while(left < right){
            if(skill[right] + skill[left] != Sum) return -1; 
            chem += (skill[right] * skill[left]);

            left++;
            right--; 
        }

        return chem; 


    }
};