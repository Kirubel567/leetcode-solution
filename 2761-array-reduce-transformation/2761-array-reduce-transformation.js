/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let accumulate = init; 
    nums.forEach((element, idx)=>{
        accumulate = fn(accumulate, element); 
    })

    return accumulate; 
};