class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> binary(n);
        
        for (int i = 0; i < n; ++i) {
            binary[i] = nums[i] % 2;
        }
        
        vector<int> prefix(n + 1, 0);
        int oddCount = 0;
        long long result = 0; 
        
        prefix[0] = 1; 
        for (int i = 0; i < n; ++i) {
            oddCount += binary[i];
            if (oddCount >= k) {
                result += prefix[oddCount - k];
            }
            prefix[oddCount]++;
        }
        
        return result;
    }
};
