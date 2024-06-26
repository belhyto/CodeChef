class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> cC;
        for(char c: magazine)
        cC[c]++;

        for(char c:ransomNote)
        {
            if(--cC[c]<0)
            {
                return false;
            }
        }
        return true;
    }
};
