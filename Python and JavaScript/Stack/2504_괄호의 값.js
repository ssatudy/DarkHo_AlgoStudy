const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  let ans = 0;
  const stack = [];
  stackLength = 0;

  const check = (parenthesis) => {
    const parenthesisValue = parenthesis === ")" ? 2 : 3;
    if (
      stackLength === 0 ||
      (parenthesis === ")" && stack[stackLength - 1] === "[") ||
      (parenthesis === "]" && stack[stackLength - 1] === "(")
    ) {
      return false;
    }
    let numSum = 0;
    while (stack[stackLength - 1] !== "(" && stack[stackLength - 1] !== "[") {
      stackLength -= 1;
      numSum += stack.pop();
    }

    if (
      (parenthesis === ")" && stack[stackLength - 1] === "(") ||
      (parenthesis === "]" && stack[stackLength - 1] === "[")
    ) {
      stack.pop();
      if (numSum === 0) {
        stack.push(parenthesisValue);
      } else {
        stack.push(numSum * parenthesisValue);
      }
      return true;
    }
    return false;
  };

  for (const parenthesis of line) {
    if (parenthesis === '(' || parenthesis === '[') {
      stack.push(parenthesis);
      stackLength += 1
      continue
    }
    if (check(parenthesis)) {
      if (stack[0] !== '(' && stack[0] !== '[') {
        ans += stack.pop();
        stackLength -= 1;
      }
      continue
    }
    ans = 0
    break
  }
  console.log(ans);
  rl.close();
});

rl.on("close", () => {
  process.exit();
});