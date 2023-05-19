const str1 = "a x a";
const str2 = "racecar";
const str3 = "Dud";
const str4 = "ohox"

function palindrome(str) {
var s = "";
    var i = str.length;
    while (i>0) {
        s += str.substring(i-1,i);
        i--;
    }
    return s;
}

var x = palindrome(str1)
console.log(x)
