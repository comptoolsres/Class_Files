#!/usr/bin/bash

# This script shows how parameters can be passed into a function

add_two () {
   # Take 2 numbers and add them, returning the sum

   num1=$1 # The first argument is $1, assign to num1 variable
   num2=$2 # The second argument is $2, assign to num2 variable 
   
   sum=$((num1 + num2))  # Add the two numbers
   return $sum  # Return the sum
}

value1=5
value2=10

add_two $value1 $value2  # Call the add_two function with 2 arguments

echo "$value1 plus $value2 is $?"  # Print the result
