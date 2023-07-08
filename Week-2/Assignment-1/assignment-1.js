// 1. max: find the max value of an array of numbers
// 2. findPosition: find the first position of the target number inside an array of numbers. The
// position should be counted starting from 0, if you can't find the target, please return -1
// Reminder: you cannot use those built-in functions like Math.max() and
// Array.prototype.findIndex() to complete this assignment, please implement it by yourself.
function max(numbers) {
    let max= numbers[0];
    for(let i=0;i<numbers.length;i++){
        if (numbers[i]>max){
            max = numbers[i] ; 
        }}
    return max;
}
function findPosition(numbers, target) {
    for (let i=0; i<numbers.length ;i++){
        if (target == numbers[i]) {
            return i;
        }         
    } 
    return -1;
}     

console.log( max([1, 2, 4, 5]) ); // should print 5
console.log( max([5, 2, 7, 1, 6]) ); // should print 7
console.log( findPosition([5, 2, 7, 1, 6], 5) ); // should print 0
console.log( findPosition([5, 2, 7, 1, 6], 7) ); // should print 2
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) ); // should print 2 (the first one)
console.log( findPosition([5, 2, 7, 1, 6], 8) ); // should print -1