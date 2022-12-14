const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on("line", (line) => {
  input.push(line.split(""));
});

rl.on("close", () => {
  // input의 두 번째 요소부터 반복문 실행
  input.slice(1).forEach((inputData) => {
    const stack = []; // stack
    let stack_length = 0; // stack 길이
    let ans = "YES";
    for (const parenthesis of inputData) {
      // '('인 경우 stack에 저장
      if (parenthesis === "(") {
        stack_length++;
        stack.push(parenthesis);
        continue;
      }
      // ')'인데 stack이 비었다면 NO 출력
      if (stack_length === 0) {
        ans = "NO";
        break;
      }
      // ')'이고 stack에 '('가 저장되어 있다면 pop
      stack_length--;
      stack.pop();
    }
    if (stack_length !== 0) {
      ans = "NO";
    }
    console.log(ans);
  });
  process.exit();
});
