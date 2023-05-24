const str = "y(3(p)p(3)r)s"

function checkPar (){
var openParens = 0
    for (var i = 0; i <  str.length; i++){
        if (str[i] === "("){
            openParens++;
        } else if (str[i] === ")"){
            openParens--;
            if (openParens < 0) {
                return false
            }
        }

    }
    return openParens === 0;
    }


console.log(checkPar(str))