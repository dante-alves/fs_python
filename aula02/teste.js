
const operador = {
    "+": (num1, num2) => num1 + num2,
    "-": (num1, num2) => num1 - num2,
}


// console.log(operador["+"](1,2));

const numeros = [1,2,3];

console.log(numeros.reduce((soma, item) => soma * item));

