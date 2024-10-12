
# Chapter 4 Data File Handling

## Table of Contents
1. [Data File Operation](#data-file-operation)
2. [File Types](#file-types)
3. [Opening and Closing Files](#opening-and-closing-files)
4. [File Modes](#file-modes)
5. [Reading Files](#reading-files)
6. [Writing Files](#writing-files)
7. [With Statement](#with-statement)
8. [Appending Files](#appending-files)
9. [Binary Files Operations](#binary-files-operations)
10. [Relative and Absolute Paths](#relative-and-absolute-paths)
11. [Tell and Seek](#tell-and-seek)
12. [CSV Files Operations](#csv-files-operations)
13. [Summary](#summary)


## Data File Operation
Open -> Read/Write -> Close

## File Types
- Text Files: Human readable, can be opened in text editors.
- Binary Files: Not human readable, can't be opened in text editors.

## Opening and Closing Files
- `open()`: Opens a file and returns a file object.
- `close()`: Closes a file.

```python
file = open('file.txt', 'r')
file.close()
```

## File Modes
- `r`: Read mode. Default mode.
- `w`: Write mode. If file doesn't exist, it creates a new file. If file exists, it truncates the file.
- `a`: Append mode. If file doesn't exist, it creates a new file. If file exists, it appends the data.
- `r+`: Read and write mode.
- `w+`: Write and read mode. If file doesn't exist, it creates a new file. If file exists, it truncates the file.
- `a+`: Append and read mode. If file doesn't exist, it creates a new file. If file exists, it appends the data.
- `b`: Binary mode. Used with other modes. Eg. `rb`, `wb`, `ab`.

## Reading Files
- `read()`: Reads the entire file.
- `readline()`: Reads a single line.
- `readlines()`: Reads all the lines and returns a list.

### Example 1
```python
file = open('file.txt', 'r')
data = file.read()
print(data)
file.close()
```

### Example 2
```python
file = open('file.txt', 'r')
data = file.readline()
print(data)
file.close()
```

### Example 3
```python
file = open('file.txt', 'r')
data = file.readlines()
print(data)
file.close()
```

## Writing Files
- `write()`: Writes a string to the file.
- `writelines()`: Writes a list of strings to the file.

### Example 1
```python
file = open('file.txt', 'w')
file.write('Hello, World!')
file.close()
```

### Example 2
```python
file = open('file.txt', 'w')
file.writelines(['Hello, World!', 'Welcome to Python!'])
file.close()
```

## With Statement
- Automatically closes the file.
- Syntax: `with open('file.txt', 'r') as file:`
- No need to call `file.close()`.
- Recommended way to open files.

### Example - Reading File
```python
with open('file.txt', 'r') as file:
    data = file.read()
    print(data)
```

### Example - Writing File
```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
```

## Appending Files
The file already exists with some data. We want to append (add more data at the end) some more data to the file.
- `a`: Append mode.

### Example
```python
with open('file.txt', 'a') as file:
    file.write('Hello, World!')
```

## Binary Files Operations

### Pickling
- Used to write dictionaries, lists, etc. to a file as they are.
- Library used is `pickle`.
- Pickling refers to the process of converting a Python object into a byte stream.
- Unpickling refers to the process of converting a byte stream back into a Python object.
- Syntax to write: `pickle.dump(data, file)`.
- Syntax to read: `data = pickle.load(file)`.

### Example - Writing
```python
import pickle

data = {'name': 'John', 'age': 22, 'city': 'New York'}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
```

### Example - Reading
```python
import pickle

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
    print(data)
```

Note: the files are stored as binary files format in the system with an extension of `.pkl`.

## Relative and Absolute Paths
- Relative Path: Path relative to the current working directory.
- Absolute Path: Complete path from the root directory.

### Example
- Relative Path: `file.txt`
- Absolute Path: `C:/Users/John/Desktop/file.txt`

## Tell and Seek
- `tell()`: Returns the current position of the cursor.
- `seek()`: Moves the cursor to a specified position.

### Example
Suppose the text file is like this:
```
Hello, World!
Welcome to Python!
```

```python
file = open('file.txt', 'r')
print(file.tell())
file.seek(5)
print(file.tell())
file.close()
```
Output:
```
0
5
```
So initially the cursor is at position 0. After `seek(5)`, the cursor moves to position 5.
If we read the file now, it will start reading from position 5. For the above example, the output will be:
```python
file = open('file.txt', 'r')
data = file.read()
print(data)
file.close()
```
Output:
```
, World!
Welcome to Python!
```
Here the cursor is at position 5, so it starts reading from position 5.

## CSV Files Operations
- Used to store tabular data.
- Library used is `csv`.

### Example - Reading CSV File
Let our CSV file be like this:
```csv
Name, Age, City
John, 22, New York
Alice, 25, Los Angeles
```

```python
import csv

filehanlder = open('data.csv', 'r')
data = csv.reader(filehanlder)

for row in data:
    print(row)

filehanlder.close()
```
Output:
```
['Name', ' Age', ' City']
['John', ' 22', ' New York']
['Alice', ' 25', ' Los Angeles']
```
Note the output will be in the form of a list. Each row of the list the row in the csv file.

### Example - Writing CSV File
```python
import csv

data = [['Name', 'Age', 'City'], ['John', 22, 'New York'], ['Alice', 25, 'Los Angeles']]

filehandler = open('data.csv', 'w', newline='')
csvwriter = csv.writer(filehandler)

for row in data:
    csvwriter.writerow(row)

filehandler.close()
```
The above code will write the data to the csv file. The csv file will look like:
```csv
Name, Age, City
John, 22, New York
Alice, 25, Los Angeles
```

## Summary
- Open a file using `open()` and close it using `close()`.
- Different file modes are `r`, `w`, `a`, `r+`, `w+`, `a+`, `b`.
- Read the file using `read()`, `readline()`, `readlines()`.
- Write to the file using `write()`, `writelines()`.
- Use `with` statement to open files.
- Append data to the file using `a` mode.
- Use `pickle` to write and read binary files.
- Use `tell()` and `seek()` to get and set the cursor position.
- Use `csv` to read and write csv files.
