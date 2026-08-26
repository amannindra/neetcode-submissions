class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> d = {};
        int n = nums.size();


        for (int i = 0; i < n; i++) {
            d[nums[i]]++;
        }

        for(int i = 0; i < d.size(); i++){
            if (d[nums[i]] > 1){
                return true;
            }
        }
        return false;
    }
};