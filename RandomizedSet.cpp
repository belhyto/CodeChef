class RandomizedSet {
    unordered_map<int,int> map_val;
    vector <int> nums;
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if(map_val.count(val))
        return false;

        nums.push_back(val);
        map_val[val]=nums.size()-1;
        return true;
    }
    
    bool remove(int val) {
        if( !map_val.count(val))
        return false;

        int index= map_val[val];
        nums[index] = nums[nums.size()-1];
        map_val[nums[index]]=index;

        nums.pop_back();
        map_val.erase(val);
        return true;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
