function shuffle(nums: number[], n: number): number[] {
    var newArr: number[] = nums.slice(n);
    var finalArr: number[] = [];
    for (var i: number = 0; i < n; i++) {
        finalArr.push(nums[i]);
        finalArr.push(newArr[i]);
    }
    return finalArr;
};