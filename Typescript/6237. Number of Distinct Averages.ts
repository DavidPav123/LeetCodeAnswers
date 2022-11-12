function distinctAverages(nums: number[]): number {
    var seen: number[] = [];
    var minValue: number = 0;
    var maxValue: number = 0;
    while (nums.length > 1) {
        minValue = Math.min(...nums);
        nums.splice(nums.indexOf(minValue), 1)
        maxValue = Math.max(...nums);
        nums.splice(nums.indexOf(maxValue), 1)
        seen.push((minValue + maxValue) / 2);
    }
    var seenSet = new Set(seen);
    return seenSet.size;
};