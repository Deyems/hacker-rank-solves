function plusMinus(arr: number[]): void {
    // Write your code here
    let positiveCount:number = 0;
    let negativeCount:number = 0;
    let zeroCount: number = 0;
    let totalCount: number = arr.length;
    
    arr.forEach((curr:number,idx:number) => {
        if(curr > 0) positiveCount++;
        else if(curr == 0) zeroCount++;
        else negativeCount++;
    });

    console.log((positiveCount/totalCount).toFixed(6));
    console.log((negativeCount/totalCount).toFixed(6));
    console.log((zeroCount/totalCount).toFixed(6));
}