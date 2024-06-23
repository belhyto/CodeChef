class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k=1;
        int c=0;
        for(int i = 1; i<nums.size(); i++ )
        {
            
            if(nums[i-1]==nums[i])
            {
                c++;
            }
            
        
            if (c<2)
            {
                nums[k++]=nums[i];
            }
             else
            c=0;
        }
     return k;      
    }
};
