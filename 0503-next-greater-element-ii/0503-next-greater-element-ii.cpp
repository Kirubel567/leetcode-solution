class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        stack<int> st;
        vector<int> answer(nums.size(), -1);   
        for(int i = 0; i < 2 * nums.size(); i++){
            int index = i % nums.size();
            while(!st.empty() && nums[st.top()] < nums[index]){
                int ind = st.top(); 
                st.pop(); 
                answer[ind] = nums[index]; 
            }
            if(i < nums.size())st.push(index); 

        }     
        return answer;    
    }
};