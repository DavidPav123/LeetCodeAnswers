function numIdenticalPairs(nums: number[]): number {
    var numPairs: number = 0;
    for (var i: number = 0; i < nums.length; i++) {
        for (var j: number = i+1; j < nums.length; j++) {
            if (nums[i] == nums[j]){
                numPairs += 1;
            }
        }
    }
    return numPairs;
};