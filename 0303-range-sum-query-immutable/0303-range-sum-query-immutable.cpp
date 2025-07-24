class NumArray {
private:
    vector<int> nums; 
public:
    NumArray(vector<int>& nums) {
        this->nums = nums; 
    }
    
    int sumRange(int left, int right) {
        int accumulate = 0; 
        int i = left; 
        while(i < right + 1){
            accumulate += nums[i]; 
            i++; 
        }
        return accumulate; 
        
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */