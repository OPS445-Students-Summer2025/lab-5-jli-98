#!/usr/bin/env python3

# Author ID: jli699 - 175495233

def read_file_string(file_name):
    f = open(file_name,'r').read();
    return f;

def read_file_list(file_name):
    f = open(file_name, 'r').readlines();
    list1 = [];
    for line in f:
        list1.append(line.strip('\n'));
    return list1;


if __name__ == "__main__":
    file_name = 'data.txt';
    print(read_file_string(file_name));
    print(read_file_list(file_name));


