

# Functions

## Table of Contents
- [Function Definition](#function-definition)
- [Built in Functions](#built-in-functions)
  - [Important Examples](#important-examples)
- [Other Functions](#other-functions)
    - [Important Examples](#important-examples-1)
- [Modules](#modules)
    - [Import Modules](#import-modules)
        - [Example: Importing the Math Module](#example-importing-the-math-module)
- [Math Module](#math-module)
    - [Important Examples](#important-examples-2)
- [Random Module](#random-module)
    - [Important Examples](#important-examples-3)
- [User Defined Functions](#user-defined-functions)
    - [Important Examples](#important-examples-4)
    - [Different Types of Arguments](#different-types-of-arguments)
        - [Positional Arguments](#positional-arguments)
        - [Keyword Arguments](#keyword-arguments)
        - [Default Arguments](#default-arguments)
        - [Variable Length Arguments](#variable-length-arguments)
- [Passing Arrays or List to Functions](#passing-arrays-or-list-to-functions)


## Function Definition

Functions are smaller modules which are used to perform a specific task. They are defined using the `def` keyword. The syntax for defining a function is as follows:

```python
def function_name():
    # code block
```

## Built in Functions
Python has many built-in functions which can be used directly. Some of the commonly used built-in functions are:
- `print()`: Used to print the output to the console.
- `input()`: Used to take input from the user.
- `len()`: Used to get the length of a string.
- `type()`: Used to get the type of a variable.
- `int()`: Used to convert a variable to an integer.
- `float()`: Used to convert a variable to a float.
- `str()`: Used to convert a variable to a string.

### Important Examples

#### Example 1: Print Function
```python
print("Hello World")
```
Output: `Hello World`

#### Example 2: Input Function
```python
name = input("Enter your name: ")
print("Hello", name)
```
Output: `Enter your name: `
        `Hello <name>`

#### Example 3: Length Function
```python
name = "John Doe"
print(len(name))
```
Output: `8`

#### Example 4: Type Function
```python
name = "John Doe"
print(type(name))
```
Output: `<class 'str'>`

#### Example 5: Integer Conversion
```python
num = "10"
print(int(num))
```
Output: `10`

#### Example 6: Float Conversion
```python
num = "10"
print(float(num))
```
Output: `10.0`

#### Example 7: String Conversion
```python
num = 10
print(str(num))
```
Output: `'10'`

## Other Functions
There are some other important functions which are used in Python. Some of them are:
- `abs()`: Used to get the absolute value of a number.
- `max()`: Used to get the maximum value from a list.
- `min()`: Used to get the minimum value from a list.
- `sum()`: Used to get the sum of all the elements in a list.
- `eval()`: Used to evaluate an expression.
- `round()`: Used to round off a number.
- `range()`: Used to generate a sequence of numbers.

### Important Examples

#### Example 1: Round Function
```python
num = 10.5
print(round(num))
```
Output: `10`

#### Example 2: Round Function with Precision
```python
num = 10.555
print(round(num, 2))
```
Output: `10.56`

Note: The second argument in the `round()` function is the precision. It specifies the number of decimal places to round off to. If the precision is not specified, the number is rounded off to the nearest integer. If the last digit is 5, the number is rounded off to the nearest even number. Example: `round(2.5)` will return `2` and `round(3.5)` will return `4`.

#### Example 3: Range Function
```python
for i in range(5):
    print(i)
```
Output: `0`
        `1`
        `2`
        `3`
        `4`

## Modules
Modules are files which contain Python code. They can be imported in other files to use the code. Python has many built-in modules which can be used directly. Some of the commonly used modules are:
- `math`: Contains mathematical functions.
- `random`: Contains functions to generate random numbers.

### Import Modules
To import a module, use the `import` keyword followed by the module name. The syntax for importing a module is as follows:

```python
import module_name
```

#### Example: Importing the Math Module
```python
import math
print(math.sqrt(16))
```
Output: `4.0`


## Math Module
The `math` module contains many mathematical functions. Some of the commonly used functions are:
- `math.sqrt()`: Used to get the square root of a number.
- `math.pow()`: Used to get the power of a number.
- `math.sin()`: Used to get the sine of an angle.
- `math.cos()`: Used to get the cosine of an angle.
- `math.tan()`: Used to get the tangent of an angle.
- `math.pi`: Contains the value of pi.

### Important Examples
#### Example 1: Square Root Function
```python
import math
print(math.sqrt(16))
```
Output: `4.0`

#### Example 2: Power Function
```python
import math
print(math.pow(2, 3))
```
Output: `8.0`


#### Example 3: Ceil Function
Note: Ceil function is used to get the smallest integer greater than or equal to a number.
```python
import math
print(math.ceil(4.1))
```
Output: `5`

#### Example 4: Log10 Function
Note: Log10 function is used to get the logarithm of a number to the base 10.
```python
import math
print(math.log10(100))
```
Output: `2.0`

## Random Module
The `random` module contains functions to generate random numbers. Some of the commonly used functions are:
- `random.random()`: Used to get a random float number between 0 and 1.
- `random.randint()`: Used to get a random integer number between two numbers.
- `random.choice()`: Used to get a random element from a list.
- `random.shuffle()`: Used to shuffle a list.
- `random.uniform()`: Used to get a random float number between two numbers.

### Important Examples
#### Example 1: Random Function
```python
import random
print(random.random())
```
Output: `0.123456789`

#### Example 2: Random Integer Function
```python
import random
print(random.randint(1, 10))
```
Output: `5`

#### Example 3: Random Choice Function
```python
import random
print(random.choice([1, 2, 3, 4, 5]))
```
Output: `3`

#### Example 4: Random Shuffle Function
```python
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
```
Output: `[3, 1, 5, 2, 4]`

#### Example 5: Random Uniform Function
```python
import random
print(random.uniform(1, 10))
```
Output: `5.123456789`

## User Defined Functions
Apart from built-in functions, we can also define our own functions. The syntax for defining a function is as follows:

```python
def function_name(parameters):
    # code block
    return value
```

Things about the above function:
- `def`: Keyword used to define a function.
- `:`: Colon is used to indicate the start of the function block.
- `function_name`: Name of the function.
- `parameters`: Arguments passed to the function.
- `return`: Keyword used to return a value from the function.

**More about return statement:**
- The `return` statement is used to return a value from the function.
- If the `return` statement is not used, the function will return `None`.
- The `return` statement can return multiple values separated by commas.

### Important Examples
#### Example 1: User Defined Function
```python
def add(a, b):
    return a + b

print(add(2, 3))
```
Output: `5`

#### Example 2: User Defined Function with Multiple Return Values
```python
def add_sub(a, b):
    return a + b, a - b

add, sub = add_sub(5, 3)
print(add,',',sub)
```
Output: `8,2`


### Different Types of Arguments
There are different types of arguments which can be passed to a function. Some of them are:
- Positional Arguments
- Keyword Arguments
- Default Arguments
- Variable Length Arguments

#### Positional Arguments
Positional arguments are the arguments which are passed to a function in the order they are defined. The number of arguments passed should match the number of parameters defined in the function.

```python
def add(a, b):
    return a + b

print(add(2, 3))
```
Output: `5`

In the example above `2` is passed as the first argument and `3` is passed as the second argument. The function `add` takes these arguments and returns the sum of the two numbers. The order of the arguments is important.

#### Keyword Arguments
Keyword arguments are the arguments which are passed to a function with the parameter name. This way the order of the arguments does not matter.

```python
def add(a, b):
    return a + b

print(add(b=2, a=3))
```
Output: `5`

In the example above `b=2` is passed as the first argument and `a=3` is passed as the second argument. The function `add` takes these arguments and returns the sum of the two numbers. The order of the arguments does not matter.

#### Default Arguments
Default arguments are the arguments which have a default value. If the argument is not passed, the default value is used.

```python
def add(a, b=0):
    return a + b

print(add(2))
```
Output: `2`

In the example above `2` is passed as the first argument and the second argument is not passed. The function `add` takes these arguments and returns the sum of the two numbers. The default value of `b` is `0`.
We can override the default value by passing a new value.

```python
def add(a, b=0):
    return a + b

print(add(2, 3))
```
Output: `5`

In the example above `2` is passed as the first argument and `3` is passed as the second argument. The function `add` takes these arguments and returns the sum of the two numbers. The default value of `b` is overridden by passing a new value.

#### Variable Length Arguments
Variable length arguments are the arguments which can take any number of values. The syntax for variable length arguments is as follows:

```python
def function_name(*args):
    # code block
```

In the syntax above `*args` is used to take any number of arguments. The arguments are stored in a tuple.

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))
```
Output: `15`

In the example above `1, 2, 3, 4, 5` are passed as arguments. The function `add` takes these arguments and returns the sum of the numbers. 

## Passing Arrays or List to Functions
Arrays or lists can be passed to functions in Python. The syntax for passing arrays or lists to functions is as follows:

```python
def function_name(array):
    # code block
```

In the syntax above `array` is the name of the array or list which is passed to the function.

```python
def add(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
print(add(numbers))
```
Output: `15`

In the example above `numbers` is an array which is passed as an argument. The function `add` takes this array and returns the sum of the numbers.


## Scope Of Variables
The scope of a variable is the region where it is defined. There are two types of variables in Python:
- Global Variables
- Local Variables

#### Global Variables
Global variables are the variables which are defined outside a function. They can be accessed from any function.

```python
x = 10

def add():
    return x + 5

print(add())
```
Output: `15`

In the example above `x` is a global variable which is defined outside the function `add`. The function `add` takes this variable and returns the sum of the variable and `5`.

#### Local Variables
Local variables are the variables which are defined inside a function. They can only be accessed from the function in which they are defined.

```python
def add():
    x = 10
    return x + 5

print(add())
```
Output: `15`

In the example above `x` is a local variable which is defined inside the function `add`. The function `add` takes this variable and returns the sum of the variable and `5`.

## Using MAIN Function
In simple words, the main function is the entry point of a program. It is the first function which is executed when a program is run. The main function is not defined in Python. We can define a main function and call it explicitly.

```python
def main():
    print("Hello World")

if __name__ == "__main__":
    main()
```
Output: `Hello World`

## Recursion
Recursion is a technique in which a function calls itself. It is used to solve problems which can be broken down into smaller problems of the same type. 

### Simple Example
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```
Output: `120`

Note: Lets do a tabular representation of the above code to understand how the recursion works:
```
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * factorial(2)
             = 5 * 4 * 3 * 2 * factorial(1)
             = 5 * 4 * 3 * 2 * 1 * factorial(0)
             = 5 * 4 * 3 * 2 * 1 * 1
             = 120
```

### Recursion vs Iteration
Recursion and iteration are two ways to solve problems. Recursion is a technique in which a function calls itself. Iteration is a technique in which a loop is used to solve problems. Both recursion and iteration have their own advantages and disadvantages.

## Summary
In this chapter, we learned about functions in Python. The topics covered in this chapter are:
- Function Definition
- Built-in Functions
- Other Functions
- Modules
- Math Module
- Random Module
- User Defined Functions
- Different Types of Arguments
- Passing Arrays or List to Functions
- Scope of Variables
- Using MAIN Function
- Recursion
- Recursion vs Iteration





