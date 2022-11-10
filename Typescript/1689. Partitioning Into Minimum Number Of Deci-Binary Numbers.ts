function minPartitions(n: string): number {
    var largestDigit = 0;
    for (var i = 0; i < n.length; i++) {
        if (parseInt(n[i]) > largestDigit) {
            largestDigit = parseInt(n[i]);
        }
    }
    return largestDigit;
};