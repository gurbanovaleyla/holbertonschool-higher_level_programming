#!/usr/bin/node

const value = process.argv[2];
const num = parseInt(value);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
