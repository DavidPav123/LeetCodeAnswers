function finalValueAfterOperations(operations: string[]): number {
    var finalVal:number = 0;
    for (var i:number = 0; i < operations.length;i++){
        if(operations[i] == "X++" || operations[i] == "++X"){
            finalVal++;
        }
        else{
            finalVal--;
        }
    }
    return finalVal;
};