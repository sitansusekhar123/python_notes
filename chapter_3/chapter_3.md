# Exception Handling

## Table of Contents
1. [Exceptions](#exceptions)
2. [Types of Exceptions](#types-of-exceptions)
3. [Raise an Exception](#raise-an-exception)
4. [Assert Statement](#assert-statement)
5. [Handling Exceptions](#handling-exceptions)
6. [Summary](#summary)

## Exceptions
- An exception is an error that occurs during the execution of a program.
- When an exception occurs, the program stops running and generates an error message.

### Example of Exception
```python
num1 = 10
num2 = 0
result = num1 / num2
print(result)
```
Output: `ZeroDivisionError: division by zero`

## Types of Exceptions
- `ZeroDivisionError`: Occurs when a number is divided by zero.
- `NameError`: Occurs when a variable is not defined.
- `TypeError`: Occurs when an operation is performed on an object of an inappropriate type. Eg. Adding a string to an integer.
- `ValueError`: Occurs when a function receives an argument of the correct type but an inappropriate value. Eg. Converting a string to an integer.
- `IndexError`: Occurs when trying to access an index that is out of range. Eg. Accessing the 4th element of a list with 3 elements.
- `KeyError`: Occurs when trying to access a key that doesn't exist in a dictionary. Eg. Accessing a key that is not present in the dictionary.
- `FileNotFoundError`: Occurs when trying to open a file that doesn't exist. Eg. Opening a file that is not present in the directory.
- `ImportError`: Occurs when an imported module is not found.


## Raise an Exception
- We can raise an exception using the `raise` keyword.
- We can raise a built-in exception or a custom exception.

### Example 1
```python
x = -1
if x < 0:
    raise Exception('x should be greater than 0')
```
Output: `Exception: x should be greater than 0`

### Example 2
```python
name = '123'
if not name.isalpha():
    raise ValueError('Name should contain only alphabets')
```
Output: `ValueError: Name should contain only alphabets`

## Assert Statement
- The `assert` statement is used to check if a condition is `True`.
- If the condition is `False`, it raises an `AssertionError` exception.

### Example
```python
x = 10
y = 20
assert x < y, 'x should be less than y'
```
Output: No output. The program runs successfully.

### Example
```python
x = 20
y = 10
assert x < y, 'x should be less than y'
```
Output: `AssertionError: x should be less than y`

## Handling Exceptions
- We can handle exceptions using the `try`, `except`, `else`, and `finally` blocks.

### Example
```python
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Division by zero is not allowed')
```
Output: `Division by zero is not allowed`

### Example
```python
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Division by zero is not allowed')
else:
    print('Division successful')
```
Output: `Division by zero is not allowed`

## Using multiple `except` blocks
- We can use multiple `except` blocks to handle different types of exceptions.

### Example
```python
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Division by zero is not allowed')
except TypeError:
    print('Unsupported operation')
```
Output: `Division by zero is not allowed`

## Using `finally` block
- The `finally` block is used to execute code whether an exception is raised or not.

### Example
```python
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Division by zero is not allowed')
finally:
    print('Execution completed')
```
Output: `Division by zero is not allowed` and `Execution completed`

## Summary
- An exception is an error that occurs during the execution of a program.
- We can raise an exception using the `raise` keyword.
- The `assert` statement is used to check if a condition is `True`.
- We can handle exceptions using the `try`, `except`, `else`, and `finally` blocks.




