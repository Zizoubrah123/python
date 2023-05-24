const arr1 = ["a", "a", "a"];
const arr2 = 

function makeFrequencyTable(){
    var expected = {};
    for(var i = 0; i < arr1.length; i++){
        if (expected.hasOwnProperty(arr1[i])){
        expected[arr1[i]]++;
}
    else {
        expected[arr1[i]] = 1;
    }
}
    return expected
}

console.log(expected = makeFrequencyTable(arr1))
console.log(expected = makeFrequencyTable(arr2))




