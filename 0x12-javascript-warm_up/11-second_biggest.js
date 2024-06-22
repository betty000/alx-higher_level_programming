#!/usr/bin/node

let args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  let nums = args.map(Number);
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
