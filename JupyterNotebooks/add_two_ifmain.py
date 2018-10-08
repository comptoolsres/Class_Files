#!/usr/bin/env python3

def add_two(a,b):
    c=a+b
    return c

def main():
    num1=float(input("Please type one number:"))
    num2=float(input("Please type another number:"))

    print(num1, "+", num2,"=", add_two(num1,num2))

if __name__ == "__main__":
    main()
