class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        new_list = nums

        for i in enumerate(nums):
            if (i[0] != (num_len - 1)) and nums[i[0]] == nums[i[0] + 1]:
                new_list[i[0]] = new_list[i[0]] * 2
                new_list[i[0] + 1] = 0

        new_list = [x for x in new_list if x!=0]
        print(len(new_list))
        num_post_len = len(new_list)


        for x in range(num_len - num_post_len):
            new_list.append(0)
        return new_list

