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

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a');
    f.write(string_of_lines);
    f.close();
    return f;

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w');
    for x in list_of_lines:
        f.write(x + '\n');
    f.close();
    return f;

def copy_file_add_line_numbers(file_name_read, file_name_write):
    read = read_file_list(file_name_read);
    f = open(file_name_write,'w');
    count = 1;
    for x in read:
        f.write(f'{count}:{x}\n');
        count += 1;
    f.close();
    return f;

if __name__ == "__main__":
    file1 = 'seneca1.txt';
    file2 = 'seneca2.txt';
    file3 = 'seneca3.txt';
    string1 = 'First Line\nSecond Line\nThird Line\n';
    list1 = ['Line 1', 'Line 2','Line 3'];
    append_file_string(file1, string1);
    print(read_file_string(file1));
    write_file_list(file2, list1);
    print(read_file_string(file2));
    copy_file_add_line_numbers(file2, file3);
    print(read_file_string(file3))


