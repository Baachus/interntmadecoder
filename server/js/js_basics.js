// Variables
let num = 5;
const name = "John";

// Functions
function showAlert(){
    alert("AHH DON'T CLICK ME");
}

function addNumbers(a, b){
    return a + b;
}

const result = addNumbers(3, 4);
console.log(result);

//datatypes
let age = 25;
const car = "Toyota";
const isStudent= true;
const array = [1, 2, 3, 4, 5];

console.log(typeof age);
console.log(typeof car);
console.log(typeof isStudent);
console.log(typeof array);

//conditionals
let x = 20;
if (x>10){
    console.log("x is greater than 10");
}
else if (x<10){
    console.log("x is less than 10");
}
else{
    console.log("x is 10");
}

//loops
for (let i = 0; i < 10; i++){
    console.log(i);
}

while (x >= 0){
    console.log(x);
    x--;
}
