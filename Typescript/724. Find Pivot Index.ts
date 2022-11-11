function pivotIndex(nums: number[]): number {
    for (var i: number = 0; i < nums.length; i++) {
        var leftSide: number = nums.slice(0, i).reduce((a, b) => a + b, 0);
        var rightSide: number = nums.slice(i + 1).reduce((a, b) => a + b, 0);
        if (leftSide == rightSide) {
            return i;
        }
    }
    return -1;
};