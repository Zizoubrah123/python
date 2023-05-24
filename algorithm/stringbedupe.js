// const str1 = "abcABCabcABCabcABC";
// const expected = 
// function debude (){
//     var expected = "";

//     for (let i = 0; i < str1.length-1; i++) {
//         if (i < 6)
//         var expected =+ str1[i]
        
//     return expected
//     }
// }

// aziz = debude();
// console.log(aziz)

const str1 = "abcABCabcABCabcABC";
const expected = 
function debude (){
    var tempObj = {};
    var newString = "";
    for (let i = 0; i < str1.length-1; i++){
        if (str1[i] in tempObj){
            temp[str1[i]] += 1;
    }
    else{
        tempObj [str1[i]] = 1;
    }
    }
    for (var key in tempObj){
        newString +=key;
    }
}
aziz = debude()
console.log(aziz)