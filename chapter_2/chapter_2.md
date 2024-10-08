# Functions

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



