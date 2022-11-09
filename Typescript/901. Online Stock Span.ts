class StockSpanner {
    test: number[];

    constructor() {
        this.test = [];
    }

    next(price: number): number {
        this.test.push(price);
        var count: number = 0;
        for (let i = (this.test.length) - 1; i >= 0; i--) {
            if (this.test[i] <= price) {
                count++;
            }
            else {
                break
            }
        }
        return count;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */