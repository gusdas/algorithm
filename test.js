const { count } = require("console");

const graph = {
  2: ['a', 'b', 'c'],
  3: ['d', 'f', 'e'],
  4: ['G', 'H', 'I'],
  5: ['j', 'k', 'l'],
};
function solution(digits) {
  if (digits.length === 0) return [];
  // global result
  const result = [];
  // alpha hash map
  const alpha = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
  };
  
  //
  // dfs recursive helper
  const dfs = (i, digits, slate) => {
    //base case
    if (i === digits.length) {
      result.push(slate.join(''));
      return;
    }
    // dfs recursive case
    let chars = alpha[digits[i]];
    for (let char of chars) {
    
      slate.push(char);
      dfs(i + 1, digits, slate);
      slate.pop();
    }
    //왜 result = ['ad' , 'ae', 'af'] 에서  i = 1이 되기전에 slate.pop()하고 slate.push(b")를하지
  };
  dfs(0, digits, []);
  print(count);
  return result;
}
let digits = '23';
console.log(solution(digits));
