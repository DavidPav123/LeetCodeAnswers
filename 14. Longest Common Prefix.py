class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            if "" in strs:
                return ""

            cur_prefix = strs[0]
            new_prefix = ""

            for word in strs:
                cur_index = 0
                word_len = len(word)
                while cur_index < word_len and len(cur_prefix) > cur_index:
                    if word[cur_index] == cur_prefix[cur_index]:
                        new_prefix = new_prefix + word[cur_index]
                        cur_index += 1
                    else: 
                        break
                cur_prefix = new_prefix
                new_prefix = ""

            return cur_prefix
