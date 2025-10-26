/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let alteredArray = []; 
    arr.forEach((element, idx)=>{
        if(fn(element, idx)){
            alteredArray.push(element); 
        }
    })
    return alteredArray; 
};