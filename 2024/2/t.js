import { createReadStream } from 'fs';
import { createInterface } from 'readline';

async function processFileLines(filePath) {
  let row = [];
  const rl = createInterface({
    input: createReadStream(filePath),
    crlfDelay: Infinity // Treat all line endings as a single delimiter
  });

  for await (const line of rl) {
    // Process each line here
    let liner = line.trim()
    liner = liner.split(" ");
    row.push(liner);
  }
    return row;
}

function checker(line) {
    let good = true;
    let prevNum = null;
    let mode = null;
    line.forEach((num) => {
        num = Number(num);
        if (prevNum === null) {
            prevNum = num;
            return;
        }
        if (num <= prevNum && prevNum - num >=1 && prevNum - num <=3 && mode !== "increasing") {
            mode = "decreasing";
            prevNum = num;
            return
        }
        if (num >= prevNum && num - prevNum >=1 && num - prevNum <=3 && mode !== "decreasing") {
            mode = "increasing";
            prevNum = num;
            return
        }
        good = false;
    });
    if (good) {
       return true;
    }
}
 // Example usage:
const row = await processFileLines('input.txt');

let goodCount = 0;
row.forEach((line) => {
    if (checker(line)) {
        goodCount += 1;
        return;
    }
    for (let i = 0; i < line.length; i++) {
        let replica = [...line];
        replica.splice(i, 1);
        console.log(replica);
        if (checker(replica)) {
            goodCount += 1;
            break;
        }
    }
});

console.log(goodCount);