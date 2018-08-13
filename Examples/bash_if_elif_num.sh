#!/bin/bash
x=$1
echo The value of x is $x 
if [ $x -lt 10 ]
then
  echo "x is small, it's only $x" 
elif [ $x -lt 100 ]
then
  echo "x is just right, it's $x"
else
  echo "x is big, it's $x”
fi
