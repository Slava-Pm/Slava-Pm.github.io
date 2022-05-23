'use strict';

/**
 * Функция возводит основание х в степень n 
 * @param {number} x - основание 
 * @param {number} n - степень
 * @returns x**n
 */
function pow(x,n){
  return x**n;  
}
//Функция,которая для данного натурального n вычисляет сумму чисел от 1 до n. 
/**
 * 
 * @param {number} n число
 * @returns сумму чисел от 1 до n
 */
function sumTo(n){
  let sum=0;
  for(let i=1;i<=n;i++){
    sum+=i;
  }
  return sum;
}

/**
 * Функция находит факториал введенного числа n
 * @param {*} n 
 * @returns 
 */
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
     //Функция,которая принимает целочисленное значение x и возвращает анонимную функцию.
//Если y больше, чем x, то возвращается true
//Если y меньше, чем x, то возвращается false
//Если значения равны, то возвращается null
function compare(x)
{
    return function(y) {
        if (y > x){
            return true;}
        if (y < x){
            return false;}
        if (x === y)
            return null;
    }}

    // pow(2, 3)