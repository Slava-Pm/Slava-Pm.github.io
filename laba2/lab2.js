'use strict';
function pow(x,n){
  return x**n;  
}

function sumTo(n){
  let sum=0;
  for(let i=1;i<=n;i++){
    sum+=i;
  }
  return sum;
}

function factorial(n){
 if(n>0)
   return (n*factorial(n-1));
   else 
     return 1;
  }
function fib(n){
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);   
}  