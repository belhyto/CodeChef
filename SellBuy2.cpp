class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sell=0;
        for(int i=1; i<prices.size(); i++)
        {
            if(prices[i]>prices[i-1])
            {
                sell+=prices[i]-prices[i-1];
            }

        }
        return sell;
    }
};
