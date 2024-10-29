Here are 50 multiple-choice questions on Python basics for a Year 12 student covering topics like loops, conditions, file I/O, stacks, functions, variables, and exception handling. The answers are provided at the end.

---

**1. Which of the following is a valid variable name in Python?**

   - A. `1st_number`
   - B. `first-number`
   - C. `first_number`
   - D. `first number`

**2. What will be the output of the following code?**

   ```python
   x = 10
   if x > 5:
       print("Greater than 5")
   else:
       print("5 or less")
   ```

   - A. Greater than 5
   - B. 5 or less
   - C. Error
   - D. None of the above

**3. Which function is used to read all lines of a file in Python?**

   - A. `readline()`
   - B. `readlines()`
   - C. `read()`
   - D. `open()`

**4. Which statement correctly represents the syntax for a `for` loop in Python?**

   - A. `for x in range(5)`
   - B. `for x from 1 to 5`
   - C. `for (x = 0; x < 5; x++)`
   - D. `for each x in range(5)`

**5. What will be the output of the following code?**

   ```python
   for i in range(1, 4):
       print(i, end=", ")
   ```

   - A. 1, 2, 3, 
   - B. 1 2 3
   - C. 1, 2, 3, 4,
   - D. 1 2 3 4

**6. What is the output of the following code snippet?**

   ```python
   def square(x):
       return x * x
   print(square(4))
   ```

   - A. 16
   - B. 8
   - C. 4
   - D. 1

**7. Which of these functions is used to add an element to the end of a list?**

   - A. `insert()`
   - B. `append()`
   - C. `add()`
   - D. `extend()`

**8. What will be the result of `3 // 2` in Python?**

   - A. 1.5
   - B. 2
   - C. 1
   - D. Error

**9. In which of the following cases will an `IndexError` be raised?**

   - A. Accessing an element of a list
   - B. Accessing an element outside the range of a list
   - C. Accessing a dictionary key
   - D. Accessing a valid string index

**10. What is the output of `print(type("Hello"))` in Python?**

   - A. `<class 'int'>`
   - B. `<class 'float'>`
   - C. `<class 'str'>`
   - D. `<class 'list'>`

**11. Which exception is raised when you try to divide by zero?**

   - A. `NameError`
   - B. `ZeroDivisionError`
   - C. `ValueError`
   - D. `IndexError`

**12. Which of the following is NOT a valid loop type in Python?**

   - A. `for`
   - B. `while`
   - C. `do-while`
   - D. `nested loop`

**13. What does the `pass` statement do in a loop?**

   - A. It terminates the loop.
   - B. It skips the rest of the loop for the current iteration.
   - C. It allows the loop to continue without doing anything.
   - D. It restarts the loop from the beginning.

**14. What is the output of the following code?**

   ```python
   x = 5
   try:
       print(x / 0)
   except ZeroDivisionError:
       print("Cannot divide by zero")
   ```

   - A. Error
   - B. 0
   - C. Cannot divide by zero
   - D. None

**15. Which of these functions can open a file for both reading and writing?**

   - A. `open(filename, "r")`
   - B. `open(filename, "w")`
   - C. `open(filename, "a")`
   - D. `open(filename, "r+")`

**16. Which method removes the last item from a list in Python?**

   - A. `remove()`
   - B. `delete()`
   - C. `pop()`
   - D. `discard()`

**17. What will be the output of the following code?**

   ```python
   i = 1
   while i < 4:
       print(i)
       i += 1
   ```

   - A. 1 2 3
   - B. 1 2 3 4
   - C. 1 2
   - D. Infinite loop

**18. Which keyword is used to handle an exception in Python?**

   - A. `try`
   - B. `catch`
   - C. `except`
   - D. `finally`

**19. Which of the following is not a Python data type?**

   - A. `int`
   - B. `float`
   - C. `real`
   - D. `str`

**20. How would you create a function that returns the square of a number?**

   - A. `def square(x): return x * x`
   - B. `def square(x): print(x * x)`
   - C. `def square: x * x`
   - D. `square = lambda x: x * x`

Here are the next 30 questions continuing from the previous set. The answers are at the end.

---

**21. What will be the output of the following code?**

   ```python
   for i in range(3):
       print(i)
   ```

   - A. 0 1 2
   - B. 1 2 3
   - C. 0 1 2 3
   - D. 1 2

**22. Which of the following is NOT a valid way to open a file in Python?**

   - A. `open("file.txt", "w")`
   - B. `open("file.txt", "a")`
   - C. `open("file.txt", "r")`
   - D. `open("file.txt", "x")`

**23. Which exception is raised when a variable is not defined in Python?**

   - A. `NameError`
   - B. `TypeError`
   - C. `ValueError`
   - D. `SyntaxError`

**24. What is the purpose of the `finally` block in exception handling?**

   - A. To handle exceptions
   - B. To execute code only if no exception occurs
   - C. To ensure code is executed regardless of an exception
   - D. To raise a custom exception

**25. What will be the output of the following code?**

   ```python
   x = 3
   y = 4
   z = x * y if x > y else y - x
   print(z)
   ```

   - A. 12
   - B. 7
   - C. 1
   - D. 4

**26. Which of the following is a mutable data type in Python?**

   - A. `int`
   - B. `tuple`
   - C. `str`
   - D. `list`

**27. Which function returns the length of a list in Python?**

   - A. `size()`
   - B. `count()`
   - C. `len()`
   - D. `length()`

**28. What will be the output of `print(2 ** 3)`?**

   - A. 5
   - B. 8
   - C. 6
   - D. 9

**29. How would you write a function that takes any number of arguments in Python?**

   - A. `def func(*args):`
   - B. `def func(args*):`
   - C. `def func():`
   - D. `def func(*):`

**30. Which of the following is the correct way to define a Python dictionary?**

   - A. `{1, 2, 3}`
   - B. `{"one": 1, "two": 2, "three": 3}`
   - C. `[1: "one", 2: "two"]`
   - D. `(1, 2, 3)`

**31. Which operator is used to check if two values are equal in Python?**

   - A. `=`
   - B. `==`
   - C. `!=`
   - D. `equals()`

**32. What will be the output of the following code?**

   ```python
   x = [1, 2, 3]
   x.append(4)
   print(x)
   ```

   - A. `[1, 2, 3]`
   - B. `[1, 2, 3, 4]`
   - C. `1, 2, 3, 4`
   - D. `[4, 1, 2, 3]`

**33. What is the result of `10 % 3` in Python?**

   - A. 3
   - B. 1
   - C. 0
   - D. 2

**34. Which Python keyword is used to create a class?**

   - A. `function`
   - B. `class`
   - C. `def`
   - D. `create`

**35. What will be the output of the following code snippet?**

   ```python
   def multiply(x, y=2):
       return x * y
   print(multiply(3))
   ```

   - A. 6
   - B. 3
   - C. 5
   - D. 2

**36. Which of these is a correct way to handle multiple exceptions in Python?**

   - A. `except (TypeError, ValueError):`
   - B. `except TypeError or ValueError:`
   - C. `except TypeError, ValueError:`
   - D. `except all errors:`

**37. What will the following code produce?**

   ```python
   try:
       print(10 / 0)
   except ZeroDivisionError:
       print("Division by zero error")
   ```

   - A. 0
   - B. Division by zero error
   - C. 10
   - D. Error

**38. How do you create a set in Python?**

   - A. `[1, 2, 3]`
   - B. `{1, 2, 3}`
   - C. `(1, 2, 3)`
   - D. `set[1, 2, 3]`

**39. Which operator would you use to check if a value exists in a list?**

   - A. `=`
   - B. `is`
   - C. `in`
   - D. `==`

**40. What will be the result of the following code?**

   ```python
   def func(a, b=5, c=10):
       return a + b + c
   print(func(3, 4))
   ```

   - A. 7
   - B. 12
   - C. 17
   - D. Error

**41. Which of the following methods is used to convert a string to lowercase in Python?**

   - A. `toLower()`
   - B. `lowercase()`
   - C. `lower()`
   - D. `makeLower()`

**42. How do you open a file for reading in Python?**

   - A. `open(filename, "w")`
   - B. `open(filename, "a")`
   - C. `open(filename, "r")`
   - D. `open(filename, "rw")`

**43. What will `print(type([]))` output?**

   - A. `<class 'list'>`
   - B. `<class 'tuple'>`
   - C. `<class 'dict'>`
   - D. `<class 'set'>`

**44. What is the output of `bool(0)` in Python?**

   - A. True
   - B. False
   - C. Error
   - D. None

**45. Which of the following is the correct way to inherit a class in Python?**

   - A. `class ChildClass(ParentClass):`
   - B. `class ChildClass inherits ParentClass:`
   - C. `class ChildClass : ParentClass`
   - D. `class ChildClass < ParentClass:`

**46. What will the following code produce?**

   ```python
   try:
       x = int("a")
   except ValueError:
       print("Value error")
   ```

   - A. Value error
   - B. a
   - C. Error
   - D. None

**47. Which of the following is used to delete an item from a dictionary?**

   - A. `delete()`
   - B. `discard()`
   - C. `pop()`
   - D. `remove()`

**48. What does `print(len("Hello"))` output?**

   - A. 4
   - B. 5
   - C. 6
   - D. Error

**49. How do you get a list of keys from a dictionary `d`?**

   - A. `d.keys()`
   - B. `keys(d)`
   - C. `d.getKeys()`
   - D. `list(d)`

**50. Which of the following is a valid way to write an infinite loop in Python?**

   - A. `while True:`
   - B. `while (1):`
   - C. `while x == x:`
   - D. All of the above

---

