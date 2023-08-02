// Create a program named 1-stdin.js that will be executed through command line:
// It should display the message Welcome to Holberton School, what is your name? (followed by a new line)
// The user should be able to input their name on a new line
// The program should display Your name is: INPUT
// When the user ends the program, it should display This important software is now closing (followed by a new line)
// Requirements:
// Your code will be tested through a child process, make sure you have everything you need for that
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log("Welcome to Holberton School, what is your name?");

// Verificar si la entrada es desde la línea de comandos o redirigida desde el comando 'echo'
const isInputFromCommandLine = process.stdin.isTTY;

rl.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  if (!isInputFromCommandLine) {
    console.log("This important software is now closing");
  }
  rl.close();
});
