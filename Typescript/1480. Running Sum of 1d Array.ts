function runningSum(nums: number[]): number[] {
    var total: number = 0;
    for (var i: number = 0; i < nums.length; i++) {
        nums[i] = nums[i] + total;
        total = nums[i];
    }
    return nums;
};