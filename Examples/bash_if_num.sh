#!/bin/bash
x=$1
echo The value of x is $x 
if [ $x -lt 10 ]
  then
    echo "x is small, it's only $x"
  else
    echo "x is big, it's $x”
fi
