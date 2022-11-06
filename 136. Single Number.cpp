#include <iostream>
#include <set>
#include <vector>

class Solution {
public:
  int singleNumber(std::vector<int> &nums) {
    int value;

    for (int i = 0; i < nums.size(); i++) {
      if (std::count(nums.begin(), nums.end(), nums[i]) != 2) {
        value = nums[i];
        break;
      }
    }

    return value;
  }
};