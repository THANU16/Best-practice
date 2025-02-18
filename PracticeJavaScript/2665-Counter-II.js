/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let sum = init;
    return {
        increment() {return ++sum;},
        decrement() {return --sum;},
        reset() {return sum = init;},
    };
};