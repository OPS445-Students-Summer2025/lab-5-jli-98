#!/usr/bin/env python3

# Author ID: jli699 - 175495233

def add(number1, number2):
    total = 0
    try:
        total = int(number1) + int(number2);
        return total;
    except ValueError:
        return 'error: could not add numbers';

def read_file(filename):
    try:
        return open(filename, 'r').readlines();
    except (FileNotFoundError):
        return 'error: could not read file';

if __name__ == "__main__":
    print(add(10,5))
    print(add('10',5))
    print(add('adc',5))
    print(read_file('seneca2.txt'));
    print(read_file('file10000.txt'));
