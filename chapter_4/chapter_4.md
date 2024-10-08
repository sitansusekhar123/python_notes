
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

