function buildArray(nums: number[]): number[] {
    var ans: number[] = [];
    for (var i = 0; i< nums.length; i++){
        ans[i] = nums[nums[i]]
    }
    return ans;
};