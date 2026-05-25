#!/usr/bin/node

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let output = '';

for (const line of languages) {
  output += line + '\n';
}

console.log(output.trim());
