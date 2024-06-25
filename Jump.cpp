class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxreach=0;
        for(int i=0; i<nums.size(); i++)
        {
            if(i>maxreach)
            {
                return false;
            }
             maxreach=max(maxreach,nums[i]+i);
        }
          return maxreach >= nums.size() - 1; //compare with last element
    }
};
