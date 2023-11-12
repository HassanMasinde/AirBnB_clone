#!/bin/bash

echo "Hi Hassan Masinde, kindly Enter your commit message"
read message


git add .
git commit -m "$message"
git push
