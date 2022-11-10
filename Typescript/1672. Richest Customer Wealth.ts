function maximumWealth(accounts: number[][]): number {
    var largetWealth: number = 0;
    for (var i: number = 0; i < accounts.length; i++) {
        var accWealth: number = accounts[i].reduce((a, b) => a + b, 0);
        if (accWealth > largetWealth) {
            largetWealth = accWealth;
        }
    }
    return largetWealth;
};