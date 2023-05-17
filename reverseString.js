// const str1 = "creature";

// function reverseString(str) {
// var reversed = "";

// for (var i = str.length - 1; i >= 0; i--  ){
//     reversed += str[i]
// }




// const str1 = "object oriented programming";


// function stringReverse(str1) {
//     var acronym = "";

//     for (var i= 0; i < str1.length; i++){
//         if (str1[i] = "")
//         str1 = str1[i+1];


    
// }

//create a new satring str=""
//iterate over the array
// each itaration we concatenate str += arr[i]


const arr1 = [1,2,3];
const seprator1 = ",";
var joined = "";
// console.log(arr1.join());
function join(arr1, seprator) {
    for (var i = 0; i < arr1.length-1 ; i++){
    joined += arr1[i] + seprator;
    }
    return joined + arr1 [arr1.length-1]
}

var ss = join(arr1,seprator1)
console.log (ss)


// const arr2 = [1,2,3];
// console.log(arr2.join(arr2,"-"));

// const arr3 = [1,2,3];
// console.log(arr3.join(arr2," - "));

// const arr4 = [1]
// console.log(arr4.join(arr2,","));

// const arr5 = [];
// console.log(arr5.join(arr2,","));



function join2(arr, seprator) {
    arr.length ? true : false
}

function join0(arr, seprator) {
    
}