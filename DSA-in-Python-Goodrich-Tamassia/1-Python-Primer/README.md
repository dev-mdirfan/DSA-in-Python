# Python Primer

- [Python Primer](#python-primer)
- [1.1 Python Overview](#11-python-overview)
  - [1.1.1 The Python Interpreter](#111-the-python-interpreter)
  - [1.1.2 Preview of a Python Program](#112-preview-of-a-python-program)
    - [1. Comments](#1-comments)
    - [2. Delimiter](#2-delimiter)
    - [3. Indentation](#3-indentation)
      - [Code Fragment 1.1: A Python program that computes a GPA](#code-fragment-11-a-python-program-that-computes-a-gpa)
- [1.2 Objects](#12-objects)
  - [1.2.1 Identifiers, Objects and the Assignment Statement](#121-identifiers-objects-and-the-assignment-statement)
    - [1. Identifier](#1-identifier)
    - [2. Dynamically Typed](#2-dynamically-typed)
    - [3. Literal](#3-literal)
    - [4. Strongly Typed](#4-strongly-typed)
    - [5. Alias](#5-alias)
  - [1.2.2 Creating and Using Objects](#122-creating-and-using-objects)
    - [1. Instantiation](#1-instantiation)
    - [2. Calling Method](#2-calling-method)
    - [3. Accessor](#3-accessor)
    - [4. Mutators / Update Methods](#4-mutators--update-methods)
  - [1.2.3 Python's Built-In Classes](#123-pythons-built-in-classes)
    - [Immutable](#immutable)
    - [1. bool Class](#1-bool-class)
    - [2. int Class](#2-int-class)
    - [3. float Class](#3-float-class)
  - [Sequence Types: The list, tuple, and str Classes](#sequence-types-the-list-tuple-and-str-classes)
    - [4. list Class](#4-list-class)
    - [5. tuple Class](#5-tuple-class)
    - [6. str Class](#6-str-class)
    - [7. The set and frozenset Classes](#7-the-set-and-frozenset-classes)
    - [8. dict Class](#8-dict-class)


# 1.1 Python Overview

- To accomplish any task by a computer we require communication with computer, by building data structures and algorithms we communicate detailed instructions to a computer.
- An excellent way to perform such communication is using high-level computer language, such as **Python**.
- The Python programming language was originally developed by **Guido van Rossum** in early **1990s**, and has since become a prominently used language in industry and education.
- The second major version of the language, **Python 2**, was released in  **2000**.
- The third major version, **Python 3**, released in **2008**.

## 1.1.1 The Python Interpreter

- Python is formally an ***interpreted*** language.
  - Commands are executed through a piece of software known as the **Python interpreter**
  - The interpreter receives a command, evaluate that command, and reports the result of the command.
  - While the interpreter can be used interactively (especially when debugging), a programmer typically defines a series of commands in advance and serves those commands in a plain text file known as ***source code*** or a ***script***. And source code is conventionally stored in a file named with `.py` suffix (example: `main.py`).
- On most operating systems, the Python interpreter can be started by typing python from the command line.
- By default, the interpreter starts in interactive made with a clean workspace.
- Commands from a predefined script saved in a file (example: `demo.py`) are executed by invoking the interpreter with the filename as an argument (example: `python demo.py`), or using an additional -i flag in order to execute a script and then enter interactive mode (example: `python -i demo.py`).
- Many **Integrated Development Environments** (IDEs) provide richer software development platforms for Python, including one named IDLE that is included with the standard Python distribution. **IDLE** provides an embedded text-editor with support for displaying and editing Python code, and a basic debugger, allowing step-by-step execution of a program while examining key variable values.

## 1.1.2 Preview of a Python Program

### 1. Comments

- Comments are annotations provided for human readers, yet ignored by Python interpreter.
- The primary syntax for comments in Python is based on use of the __`#`__ character, which designates the remainder of the line as a comment.

### 2. Delimiter

- Delimiter is a sequence of one or more characters used to specify the boundary between separate.
- Whitespace is also key in **delimiting** the bodies of control structures in Python.
- Specifically, a block of code is intended to designate it as the body of a control structure, and nested control structures use increasing amounts of **indentation**.

### 3. Indentation

- Python's syntax relies heavily on the use of white space.
- It refers to the spaces at the beginning of a code line.
- Python uses indentation(Tab) to indicate a block of code for every particular reserved words in Python.
- Individual statements are typically concluded with a newline character, although a command can extend to another line, either with a concluding backslash character (__`\`__), or if an opening **delimiter** has not yet been closed, such as the __`{`__ character in defining ***value_map***.

#### Code Fragment 1.1: A Python program that computes a GPA

- let us take example of a Python program that computes the grade-point average (GPA) for a student based on letter grade that are entered by a user.

```py
# program that computes the grade-point average (GPA) for a student based on letter grade that are entered by a user.
print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# map from letter grade to point value
points = {'A+':4.0, 'A':4.0, 'A-':3.67,
          'B+':3.33, 'B':3.0, 'B-':2.67,
          'C+':2.33, 'C':2.0, 'C-':1.67,
          'D+':1.33, 'D':1.0, 'F':0.0
         }
num_courses = 0
total_points = 0
done = False

while not done:
    grade = input()                 # read line from user
    if grade == '':                 # empty line was entered
        done = True
    elif grade not in points:       # unrecognized grade entered
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
    if num_courses > 0:             # avoid division by zero
        print('Your GPA is {0: .3}'.format(total_points / num_courses))
```

```yml
Input :
A+
C-
D

Output :
Welcome to the GPA calculator.
Please enter all your letter grades, one per line.
Enter a blank line to designate the end.
Your GPA is  4.0
Your GPA is  2.83
Your GPA is  2.22
Your GPA is  2.22
```

# 1.2 Objects

- Python is an object-oriented language and **classes** from the basis for all data types.
- Python has built-in classes, such as the __`int`__ class for integers, the __`float`__ class for floating-point values, and the __`str`__ class for character strings.

## 1.2.1 Identifiers, Objects and the Assignment Statement

- The most important of all Python commands is an **assignment statement**, such as -

```py
temperature = 98.6
```

- This command establishes temperature as an __identifier__ (also known as __name__), and then associates it with the **object** expressed on the right-hand side of the equal sign, in this case a floating-point object with value 98.6.

|float|
|---|
|98.6|

⬆️
temperature

**Figure 1.1:** The identifier `temperature` references an instance of the float class having value 98.6.

### 1. Identifier

- Identifiers in Python are __case-sensitive__. so temperature and Temperature are distinct names.
- Identifier can be composed of almost any combination of letters, numerals, and underscore characters (or more general _Unicode_ characters).
- The primary restriction are that an identifier cannot begin with a numeral (thus __9lives__ is an __illegal__ name).
- There are 33 specially reserved words that cannot be used as identifiers.

**Table 1.1:** A list of the reserved words in Python. These names cannot be used as identifier.

|Reserved Words 7|Reserved Words 7|Reserved Words 7|Reserved Words 7|Reserved Words 5|
|---|---|---|---|---|
|None|for|pass|class|try|
|and|while|break|assert|except|
|or|if|continue|def|finally|
|not|elif|from|del|raise|
|in|else|import|lambda|with|
|is|True|global|yield||
|as|False|nonlocal|return||

- The semantics of a Python identifier is most similar to a **reference variable** in Java or a **pointer variable** in C++.
- Each identifier is implicitly associated with the **memory address** of the object to which it refers.
- A Python identifier may be assigned to a special object named `None`, serving a similar purpose to a null reference in Java or C++.

### 2. Dynamically Typed

- Unlike Java and C++, Python is a **dynamically typed** language, as there is no advance declaration associating an identifier with a particular data type.
- Dynamic typing means that the type of the variable is determined only during runtime.
- Due to dynamic typing, in Python the same variable can have a different type at different times during the execution. Dynamic typing allows for flexibility in programming, but with a price in performance.
- An identifier can be associated with any type of object, and it can later be reassigned to another object of the same (or different) type.
- Although an identifier has no declared type, the object to which it refers has a definite type.
- In our first example, the character 98.6 are recognized as a floating-point literal, and thus the identifier temperature is associated with an instance of the float class having that value.

### 3. Literal

- Python literals are quantities/ notations whose value does not change during the execution of a program.
- Literals in Python are nothing but a succinct way of representing the data types. In simpler words, it is the way to represent a fixed value in our source code. They can either be numbers, text, boolean or any other form of data.
- We have the concept of **constants** in Python as well! They are known as literals in Python.
- There are five types of literal in Python, which are as follows-
  1. **String Literals :** Single-line String, Multi-line String.
  2. **Numeric Literals :** Integer, Float, Complex, Long.
  3. **Boolean Literals :** True, False.
  4. **Special Literals :** None
  5. **Literal Collections :** List Literals, Tuple Literals, Dictionary Literals, Set Literals.

### 4. Strongly Typed

- Strong typing means that variables do have a type and that the type matters when performing operations on a variable.
- Due to strong typing, types need to be compatible with respect to the operand when performing operations. For example Python allows one to add an integer and a floating point number, but adding an integer to a string produces error.

### 5. Alias

- A programmer can establish an **alias** by assigning a second identifier to an existing object.

**Example :** Identifier temperature and original are aliases for the same object -

```py
temperature = 98.6
original = temperature
```

**Figure 1.2:** Identifiers temperature and original are aliases for the same object.

|float|
|---|
|98.6|
⬆️ ⬆️ original
temperature

- Once an alias has been established, either name can be used to access the underlying object.
- If that object supports behaviors that affect its state, changes enacted through one alias will be apparent when using the other alias (because they refer to the same object).
- However, if one of the names is reassigned to a new value using a subsequent assignment statement, that does not affect the aliased object, rather it breaks the alias.

```py
temperature = 98.6
original = temperature
temperature = temperature + 5.0
print(temperature, original)
```

**Output :** 103.6 98.6

- The execution of this command begins with the evaluation of the expression on the right-hand side of the = operator.
- That expression, `temperature + 5.0`, is evaluated based on the existing binding of the name temperature, and so the result has value 103.6. That result is stored as a new floating-point instance, and only then is the name on the left-hand side of the assignment statement, temperature, (re)assigned to the result.
- Of particular note, this last command had no effect on the value of the existing float instance that identifier original continues to reference.

**Figure 1.3:** The temperature identifier has been assigned to a new value, while original continues to refer to the previously existing value.

|float|
|---|
|103.6|
⬆️ temperature

|float|
|---|
|98.6|
⬆️ original

- Here, is the example of the deep copy and shallow copy

```py
temperature = 98.6
original = temperature
original = 10
print(temperature, original)
```

**Output :** 98.6 10

```py
d1 = {'a':1, 'b':2}
d2 = d1
print(id(d1)==id(d2))
del d2['b']     # del d1['b']
print(d1, d2)
```

**Output :**
True
{'a': 1} {'a': 1}

- Here, original and d2 both second alias refers to same object which assigned but `original` assigned to new object and d2 is still refers to same object so any changes in d2 reflects changes in both (d1 and d2).

## 1.2.2 Creating and Using Objects

### 1. Instantiation

- The process of creating a new instance of a class is known as **instantiation**.
- In general, the syntax for instantiating an object is to invoke the **constructor** of a class.
- For Example, If there were a class named `Widget`, we could create an instance of that class using a syntax such as `w = Widget()`, assuming that the constructor does not require any parameters. If the constructor does require parameters, we might use a syntax such as `Widget(a, b, c)` to construct a new instance.

**Literals :**

```py
temperature = 98.6 
```

- Literal form for designating new instances.
- For example, the command temperature = 98.6 results in the creation of a new instance of the **float** class.
- The term 98.6 in that expression is a literal form.

- From Programmer's perspective, yet another way to indirectly create a new instance of a class is to call a function that creates and returns such as instance.
- For example, Python has a built-in function named sorted() that takes a sequence of comparable elements as a parameter and returns a new instance of the **list** class containing those elements in sorted order.

### 2. Calling Method

- Python supports traditional functions that are invoked with a syntax such as sorted(data), in which case data is a parameter sent to the function.
- Python's classes may also define one or more **methods** (also known as **member functions**), which are invoked on a specific instance of a class using dot (".") operator.
- For example, Python's list class has a method named sort that can be invoked with a syntax such as data.sort(). This particular method rearranges the content of the list so that they are sorted.

```py
data.sort()
```

- The expression to the left of the dot identifies the object upon which the method is invoked.
- Often, this will be an identifier (e.g. data), but we can use the dot operator to invoke a method upon the immediate result of some other operation.
- For example, if response identifies a string instance -

```py
response = "Younger Brother"
response.lower().startswith('y')
```

- The syntax response.lower().startswith('y') first evaluates the method call, response.lower(), which itself returns a new string instance, and then the startswith('y') method is called on that intermediate string.

- When using a method of a class, it is important to understand its behavior.

### 3. Accessor

- Some methods return information about the state of an object, but do not change that state. These are known as **accessors**.

### 4. Mutators / Update Methods

- Other methods, such as the sort method of the list class, do change the state of an object. these methods are known as **mutators** or **update method**.

## 1.2.3 Python's Built-In Classes

### Immutable

- A class is **immutable** if each object of that class has a fixed value upon instantiation that cannot subsequently be changed.
- For example - The float class is immutable.
- Once an instance has been created, its value cannot be changed (although an identifier referencing that object can be reassigned to a different value).

**Table 1.2:** Commonly used built-in classes for Python

|Class|Description|Immutable?|
|---|---|---|
|**bool**|Boolean value|✔️|
|**int**|integer (arbitrary magnitude)|✔️|
|**float**|floating-point number|✔️|
|**list**|mutable sequence of objects||
|**tuple**|immutable sequence of objects|✔️|
|**str**|character string|✔️|
|**set**|unordered set of distinct objects||
|**frozenset**|immutable from of set class|✔️|
|**dict**|associative mapping (aka dictionary||

- Literal forms (such as 98.6) exist for most of the built-in classes, and all of the classes support a traditional constructor from that creates instances that are based upon one or more existing values.

### 1. bool Class

- The **bool** class is used to manipulate logical (Boolean) values, and the only two instances of that class are expressed as the literals **True** and **False**.
- The default constructor, `bool()`, return False, but there is no reason to use that syntax rather than more direct literal form.

```Python
flag = bool()
print(flag)
```

- Python allows the creation of a Boolean value from a non boolean type using the syntax `bool(foo)` for value foo.

```py
foo = 0     # zero
print(bool(foo))

foo = 12      # non-zero value
print(bool(foo))
```

**The interpretation depends on the type of the parameter :**

- Number evaluate to False if zero, and True if nonzero.

```py
num = 23      # Number
print(bool(num))
```

- Sequences and other container types, such as strings and lists, evaluate to False if empty and True if nonempty.

```py
sequenceBool = bool(list())       # Empty sequence datatype
print(sequenceBool)

sequence = bool('Hello World!')
print(sequence)
```

- An important application of this interpretation is the use of a non boolean value as a condition in a control structure.

### 2. int Class

- A

### 3. float Class

- B

## Sequence Types: The list, tuple, and str Classes

### 4. list Class

- C

### 5. tuple Class

- D

### 6. str Class

- E

### 7. The set and frozenset Classes

- G

### 8. dict Class

- H

