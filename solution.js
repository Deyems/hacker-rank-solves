function plusMinus(arr) {
    // Write your code here
    const result = arr.reduce((prev, cur, currentIdex, arr) => {
        if (arr[currentIdex] < 0) {
            prev.negative += 1;
        }
        else if (arr[currentIdex] > 0) {
            prev.positive += 1;
        }
        else {
            prev.zero += 1;
        }
        return prev;
    },
        {
            positive: 0,
            negative: 0,
            zero: 0
        }
    )
    const values = (Object.values(result));
    values.forEach(el => {
        console.log((el / arr.length).toFixed(6))
    })

}