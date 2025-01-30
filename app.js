// Pure functionS---------

// function add(a, b) {
//   return a + b;
// }

// // Example usage:
// console.log(add(2, 3)); // Always returns 5
// console.log(add(2, 3)); // Always returns 5


// // Impure Functions-----------

// let count = 0;
// function increment() {
//   count++;
//   return count;
// }

// console.log(increment()); // Output depends on the current state of `count`
// console.log(increment()); // Output depends on the current state of `count`


// let sol=hello()
// function hello(){
//   var c=205;
//   console.log(c)
// }

// let z=25
// a()
// function a(){
//   console.log(z)
//   var c=20
//   console.log('hello world....')
// }


let a =20
console.log(a)
var b=25;
const c=44;



function longestSubarrayWithSumMultipleOfK(arr, k) {
    let modMap = new Map();
    let prefixSum = 0;
    let maxLen = 0;
    
    for (let i = 0; i < arr.length; i++) {
        // Update the prefix sum
        prefixSum += arr[i];
        
        // Calculate modulo of the current prefix sum with k
        let mod = prefixSum % k;
        
        // If the modulo is negative, adjust it to be positive
        if (mod < 0) {
            mod += k;
        }
        
        // If mod is 0, it means the subarray from the start to current index is divisible by k
        if (mod === 0) {
            maxLen = i + 1;
        } else if (modMap.has(mod)) {
            // If mod has been seen before, calculate the length of the subarray
            maxLen = Math.max(maxLen, i - modMap.get(mod));
        } else {
            // If mod hasn't been seen, store its first occurrence
            modMap.set(mod, i);
        }
    }
    
    return maxLen;
}
let arr = [23, 2, 4, 6, 7];
let k = 6;

console.log(longestSubarrayWithSumMultipleOfK(arr, k));  // Output: 4


function reverseWords(sentence) {
    // Step 1: Split the sentence into words
    let words = sentence.split(' ');
    
    // Step 2: Reverse the words using two pointers (without using reverse)
    let left = 0;
    let right = words.length - 1;
    
    while (left < right) {
        // Swap the words
        let temp = words[left];
        words[left] = words[right];
        words[right] = temp;
        
        // Move the pointers towards the center
        left++;
        right--;
    }
    
    // Step 3: Join the words back into a sentence
    return words.join(' ');
}

// Example usage
let sentence = "The quick brown fox jumps over the lazy dog";
let reversedSentence = reverseWords(sentence);
console.log(reversedSentence);  // Output: "dog lazy the over jumps fox brown quick The"
