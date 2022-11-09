#include <iostream>

using namespace std;

class Solution {
public:
  string makeGood(string s) {
    if (s.length() > 1) {
      for (int i = 0; i < ((int)s.length()) - 1; i++) {
        if (s[i] < 95) {
          if (s[i + 1] == s[i] + 32) {
            s.erase(i, 2);
            i = -1;
          }
        } else if (s[i] > 95) {
          if (s[i + 1] == s[i] - 32) {
            s.erase(i, 2);
            i = -1;
          }
        }
      }
      return s;
    } else {
      return s;
    }
  }
};