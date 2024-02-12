#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (factorial(number - 1) * number);
  }
}

if (num) {
  const res = factorial(num);
  console.log(res);
} else {
  console.log(1);
}
