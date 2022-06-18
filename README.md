# OSSU-PY4E
First module of the "Introduction to programming" of the OSSU study curriculum of Computer Science


April 18
1. Installing Python and running my first program
2. Variables, expressions and statements*



NOTES
2* Python Concatenate String and int
Error get when tried to print(str + int) 
TypeError: cannot concatenate 'str' and 'float' objects.

Explanation: Python supports string concatenation using + operator. In most of the programming languages, if we concatenate a string with an integer or any other primitive data types, the language takes care of converting them to string and then concatenate it. However, in Python, if you try to concatenate string and int using + operator, you will get a runtime error.

Solution
Convert int into str before print.
print(s + str(y))
