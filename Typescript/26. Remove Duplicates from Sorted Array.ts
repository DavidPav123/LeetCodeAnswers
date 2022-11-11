function removeDuplicates(nums: number[]): number {
    for (var i: number = 0; i < nums.length; i++) {
        for (var j: number = i + 1; j < nums.length; j++) {
            if (nums[j] == nums[i]) {
                nums.splice(j, 1);
                j -= 1;
            }
        }
    }
    return nums.length
};