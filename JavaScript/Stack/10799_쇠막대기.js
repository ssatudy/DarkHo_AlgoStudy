const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const parenthesisLength = line.length;
  let ans = 0;
  let stickCnt = 0;
  let idx = 0;
  while (idx <= parenthesisLength - 1) {
    if (line[idx] === "(" && line[idx + 1] === ")") {
      ans += stickCnt;
      idx += 2;
      continue;
    }
    if (line[idx] === "(") {
      ans += 1;
      stickCnt += 1;
    } else if (line[idx] === ")") {
      stickCnt -= 1;
    }
    idx += 1;
  }
  console.log(ans);
  rl.close();
});

rl.on("close", () => {
  process.exit();
});