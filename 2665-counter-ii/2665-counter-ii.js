/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let original=init
    let a=function(){
        init=init+1;
        return init
    }
    let b=function(){
        init=original
        return init
    }
    let c=function(){
        init=init-1
        return init
    }
    return {
    increment: a,
    reset: b,
    decrement: c
}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */