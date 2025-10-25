/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let res = []; 
    arr.forEach((element, idx)=>{
        res.push(fn(element, idx)); 
    })

    return res; 
};