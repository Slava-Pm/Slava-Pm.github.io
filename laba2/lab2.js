'use strict';
//Функция возводит основание х в степень n
function pow(x,n){
  return x**n;  
}
//Функция,которая для данного натурального n вычисляет сумму чисел от 1 до n. 
function sumTo(n){
  let sum=0;
  for(let i=1;i<=n;i++){
    sum+=i;
  }
  return sum;
}
//Функция находит факториал введенного числа n
function factorial(n){
 if(n>0)
   return (n*factorial(n-1));
   else 
     return 1;
  }
  //Функция возвращает n-ое число Фибонначи
function fib(n){
        let a = 1n;
        let b = 1n;
        //Исключения
        if (n==0) return 0;
        if (n==1) return 1;
        if (n==2) return 1;
        for (let i = 3; i <= n; i++) {
          let c = a + b;
          a = b;
          b = c;
        }
        return b;
      }