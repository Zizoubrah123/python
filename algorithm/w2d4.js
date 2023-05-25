const newInv1 =[
    {name: "grain of rice", quantity: 9000},
    {name: "peanet butter", quantity: 50},
    {name: "rolay jelly", quantity: 20},
];

const currInv1 =[
    {name: "grain of rice", quantity: 9000},
    {name: "peanet butter", quantity: 50},
]
0
const expected =[
    {name: "grain of rice", quantity: 9001},
    {name: "peanet butter", quantity: 70},
    {name: "rolay jelly", quantity: 20},
];

function update(newInv1, currInv1) {
    for (var j = 0; j < newInv1.length; i++ ){
        var itemFound = false;
        var newitem = newInv1[i]
    for (var j = 0; j < currInv1.length; i++ ){
        var curritem = currInv1[j]

        if (newInv1.name === currInv1.name)
            itemFound = true;
        }
}
}

console.log(update())