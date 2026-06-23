/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let f=[]
    for(let i=0;i<arr.length;i++){
        if(fn(arr[i],i)){
            f.push(arr[i])
        }
        
    }
    return f
}