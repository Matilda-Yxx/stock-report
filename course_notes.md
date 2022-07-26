Section 1
=======

Introduction
-----------
You can run python in 2 modes: interactive or run as a script. Even when running a script, you can use interactive mode via `python3 -i FILE_NAME.py`. It is good to learn python using Terminal, but when doing real projects, it's easier to use an IDE such as Jupyter notebook.

* in interactive mode, `-` holds last result.
* Use `dir(object_name)` to check the available methods!

Mutability
-----------

This is one of the most important feature of a data type. If a type is immutable, each operation that attempts to modify its content would create a new instance of the original variable. You need to reassign this new instance to a new variable, or simply replace the original variable, in order to use it.

When chosing the right data type, mutability is an important consideration.

* **Mutable** data types include: List, dictionary, set
* **Immutable** data types include: Strings, tuple


Pass by reference / value
-----------

* Note that arguments are passed by assignment. (https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference) Beware if the argument you passed around is mutable or immutable!

String
-----------
* Byte strings
* Raw strings (don't interpret `\`)
* Formatted strings (this is useful!) `a = f'{name:>10s} {shares:10d} {price:10.2f}'`
* printing without starting a new line: `print(line, end=' ')`

List
-----------
* Holds any type of data
  * Even nested lists
* List "math": `a = b * 5` -> to repeat list b for 5 times
* methods
  *  `join`: `a = ','.join(symlist)`
  *  `split`: `list = a.split(',')`
  *  `sort`: `list.sort(reverse=True)`. Note that since lists are mutable, sorting is done in-place!
  *  membership tests: `not in`, `in`


File 
-----------
* Best practice is to close the file after opening.
  * to avoid forgetting to close the files, here is the best practice:
```python
  with open(filename, 'rt') as file:
      # Use the file `file`
      ...
      # No need to close explicitly
  ...statements
```
* common methods used
  * `for line in files:`
  * `next(file)`: to grab the next line from the file; may need this to process headers



Section 2
=======

2.1 Tuple, Dictionary
-----------
* `Tuple`: Useful method: packing, unpacking
* `Dictionaries` are useful when there are many different values and those values might be modified or manipulated. 
  * As compared to tuples, dictionaries make your code more readable.
  * aka: Hash table; associative array
* Useful method: `.items()`
* `key` must be an immutable object!
* `pprint` is very useful for cleaning up the output (`from pprint import pprint`).

Some additional dictionary operations:
* to obtain a list of keys from the dictionary:
  * `list(d)`
  * `for k in d:`
  * `d.keys()`
* to get items from the dictionary: `d.items()`

2.2 Containers: lists, sets, and dictionaries
-----------
* Choice of containers
  * Lists. Ordered data.
  * Dictionaries. Unordered data.
  * Sets. Unordered collection of unique items.
* `Sets`: Contains *unique* items
* `Sets` are therefore useful for duplicate elimination.

* Syntax for building a set is rather unique:
  * `tech_stocks = { 'IBM','AAPL','MSFT' }`
  * `tech_stocks = set(['IBM', 'AAPL', 'MSFT'])`

2.3 Formatting
-----------
Common format codes:
```
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
```

Common modifiers:
```
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```

And lastly, C-style formatting:
* `'%5d %-5d %10d' % (3,4,5)`

2.4 Sequence datatypes
-----------
* String, List, Tuple
* Methods of a sequence:
  * Indexing
  * replication
  * concatenation
  * slicing (end is not included)
    * Since lists are mutable, we could do slice re-assignment on list objects
    * Note that the reassigned slice does NOT need to have the same length!
  * `enumerate`
  * `zip() function`: Normally, zip() creates an iterator that must be consumed by a for-loop.
    * list(zip(headers, row)): with this, you could easily convert from dict to a list. Then you could apply any sequence functions to it!
    * dict(zip(headers, row))
    * be aware that zip() stops once the shortest input sequence is exhausted.

2.5 Collections
-----------
* The `collections` module might be one of the most useful library modules for dealing with special purpose kinds of data handling problems such as **tabulating** and **indexing**.
* The `Counter()` object is very similar to Dictionary, except that for each key you get a default value of one!
  * `Counter` objects have many useful methods, including but not limited to: `+`, `most_common(n)`
* with `defaultdict`, you can even create one-to-many mappings.

2.6 List Comprehension
-----------
**List comprehensions are hugely useful!!**
* Syntax for buiding lists: `[ <expression> for <variable_name> in <sequence> if <condition>]` (note the square brackets)
* Syntax for buiding sets: `{<expression> for <variable_name> in <sequence> if <condition>}`
* Syntax for buiding dictionaries: `{ name:0 for name in <sequence> if <condition>}`
* Syntax for buiding a tuple: `Tuple([name:0 for name in <sequence> if <condition>])`
  * If you do something like `b = (2*x for x in a)`, then b is actually a generator!
* *Becoming a guru master of list comprehensions can substantially reduce the time spent devising a solution!*

What's the code below trying to do here?
```python
>>> import csv
>>> f = open('Data/portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)

>>> select = ['name', 'shares', 'price']
>>> indices = [ headers.index(colname) for colname in select ]
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
```
Solution is [here](https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/06_List_comprehension.html).


2.7 [Objects](https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/07_Objects.html)
-----------
* In python, assignment operations **never make a copy** of the value being assigned. 
* All assignments are merely reference copies (or pointer copies if you prefer). 
* This means that **modifying** a value **affects all** references.
* **Reassigning** a value **never overwrites** the memory used by the previous value.
* use `is` to check if two values are exactly the **same object**; use `==` to check if two **values** are exactly the same.
* Remember: **Variables are names, not memory locations.** You can use `type()` to check the underlying type of the value.

**Shallow vs Deep copies**
Firstly, a shallow example:
```python
{
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Make a copy
>>> a is b
False
# It’s a new list, but the list items are shared.
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
}
```
How about a deep copy:
```python
{
>>> a = [2,3,[100,101],4]
>>> import copy
>>> b = copy.deepcopy(a)
>>> a[2].append(102)
>>> b[2]
[100,101]
>>> a[2] is b[2]
False
}
```

* The crazy thing here is that: EVERYTHING IN PYTHON IS AN OBEJCT
  * Yes you can do this: `items = [abs, math, ValueError ]`
* You could extend this by streamling type conversions [SO NEAT!!!]: 
  * `types = [str, int, float]`
  * `converted = [func(val) for func, val in zip(types, row)]`


Section 3: Functions
=======

3.1
* type annotations: `def read_prices(filename: str) -> dict:`

3.2 Functions
-----------
*  If mutable data types are passed as input arguments (e.g. lists, dicts), they can be modified **in-place**.
Beware of the difference between **modifying** and **reassigning**!!
```python
  def foo(items):
      items.append(42)    # Modifies the input object

  a = [1, 2, 3]
  foo(a)
  print(a)                # [1, 2, 3, 42]

  # VS
  def bar(items):
      items = [4,5,6]    # Changes local `items` variable to point to a different object

  b = [1, 2, 3]
  bar(b)
  print(b)                # [1, 2, 3]
```

3.3 Error Checking
-----------
* it’s better to catch the error as **narrowly** as is reasonable
* Use `raise` to propagate a caught error.
* **Don't catch errors unless it's where you can recover and sanely keep going.**
* In modern code, `try-finally` is often replaced with the `with` statement.
* Error handling is one of the most difficult things to get right in most programs!!

3.4 Modules
-----------
* Importing a module runs its code!
* **Caution**: A common confusion arises if you repeat an import statement after changing the source code for a module. Because of the module cache sys.modules, repeated imports always return the previously loaded module–even if a change was made. The safest way to load modified code into Python is to quit and restart the interpreter.
* modify/view module search path
```python
  import sys
  sys.path.append('/project/foo/pyfiles')
```

3.5 Main Module
-----------
* Add `#!/usr/bin/env python3` and `#name.py` to your script such that Unix would launch this script as Python.
* Main programs vs. library imports
  * Usually, you don’t want statements that are part of the main program to execute on a library import. So, it’s common to have an if-check in code that might be used either way.
```python
if __name__ == '__main__':
    # Does not execute if loaded with import ...
```

3.6 Design
-----------
* Duck typing (https://cloud.tencent.com/developer/article/1484390)



Section 4 Classes
=======
4.1 Classes
-----------
* Class scoping
  * This works in a DIFFERENT way from Java.
  * Classes do not define the scope of names!!
```python
class Player:
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NO. Calls a global `move` function
        self.move(-amt, 0)  # YES. Calls method `move` from above.
```

4.2 Inheritance
-----------
* Overriding, but still want to call parent method:
```python
class Stock:
  ...
  def cost(self):
      return self.shares * self.price
  ...

class MyStock(Stock):
    def cost(self):
        # Check the call to `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

* `__init__` and inheritance
If `__init__` is redefined, it's essential to initialize the parent using `super().__init__`.

Reflections:
> Another somewhat deeper concept is the idea of “owning your abstractions.” In the exercises, we defined our own class for formatting a table. You may look at your code and tell yourself “I should just use a formatting library or something that someone else already made instead!” No, you should use BOTH your class and a library. Using your own class promotes loose coupling and is more flexible. As long as your application uses the programming interface of your class, you can change the internal implementation to work in any way that you want. You can write all-custom code. You can use someone’s third party package. You swap out one third-party package for a different package when you find a better one. It doesn’t matter–none of your application code will break as long as you preserve keep the interface. That’s a powerful idea and it’s one of the reasons why you might consider inheritance for something like this.



4.3 Special Methods
-----------
* Various parts of Python’s behavior can be customized via special or so-called “magic” methods. 
* Special Methods are always preceded and followed by `__`. For example `__init__`.

Invoking a method is a two-step process.
```python
{
    >>> s = Stock('GOOG',100,490.10)
    >>> c = s.cost  # Lookup
    >>> c
    <bound method Stock.cost of <Stock object at 0x590d0>>
    >>> c()         # Method call
    49010.0
}
```
To invoke a method, rmb to attach the **trailing parentheses**!!!
* Attribute access
```python
getattr(obj, 'name')          # Same as obj.name
setattr(obj, 'name', value)   # Same as obj.name = value
delattr(obj, 'name')          # Same as del obj.name
hasattr(obj, 'name')          # Tests if attribute exists
```
This can come very handy!!

4.4 Exceptions
-----------
* It is often good practice for libraries to **define their own exceptions**.
* This makes it easier to distinguish between Python exceptions raised in response to **common programming errors** versus exceptions intentionally raised by a library to a signal a **specific usage problem**.

Section 5 Inner workings of python objects
=======

5.1 Dictionaries Revisited
----------------
* A fundamental design concept in python is that the Python object system is largely based on an implementation involving dictionaries.
```python
>>> # a dictionary that holds the instance data.
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
>>> Stock.__dict__ # holds the class methods
{
    'cost': <function>,
    'sell': <function>,
    '__init__': <function>
}
>>> s.__class__
<class '__main__.Stock'>
```

* The inner working of single inheritance: `instance.__bases__` store the parent classes.
* Multiple inheritance is a bit more complicated. There is a specific order called MRO, Method Resolution Order, to which python look thorugh the base classes (e.g. when you call a method from a class, python would start looking for the method from itself, then its parents.)
* `mixin` pattern (usually used in multiple inheritance)
```python
# suppose you have 2 irrelevant classes that wanna share a similar method
# class 1
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

# class 2
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

# the MIXIN pattern: a class with a fragment of code. a class that's NOT usable in isolation
class Loud:
    def noise(self):
        return super().noise().upper() 

# to use it, have to MIX it with other classes via inheritance
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

5.2 Encapsulation
------------------
* Python really doesn’t place any restrictions on attributes!!! 
  * For example, the attributes of an instance are not limited to those set up in the __init__() method.
  * Python also does NOT enforce any restrictions on attribute types...
  * Python does NOT enforce any PRIVATE attributes. Python relies on programming conventions to indicate the intended use of something (e.g. `_name` is a private attribute that you aren't supposed to reset with `._name`.)

* What if you wanna add certain restrictions to the attributes?
  * This can be achieved through the usage of `@property` and `@attribute_name.setter` decorators.
```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```
* If you add `@property` to some other methods, you can get rid of the parentheses when you call them:
```python
  @property
  def cost(self):
      return self.shares * self.price
  ...    
  >>> s.cost # 49017.0

```

* Restricting the set of attribute names: use `___slots__`
  * It should be noted that __slots__ is most commonly used as an optimization on classes that serve as **data structures**. You should probably avoid __slots__ on most other classes however.


Section 6 Generators
=======

6.1 Iteration Protocol
-----------
* Use `@property` to use a method without parentheses.
* `__iter__()` get you an iterator object.
  * You can customize the `__iter__()` method for your class such that it become iterable.
* `__next__()` is the underlying method of extracting the following item in an iterable object.

Self-defined iterators within a class:
```python
class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()
    ...

port = Portfolio()
for s in port:
    ...
```
Additionally, you could make your container even more accessible by creating special methods like `__len__`(then you can do `len(x)`), `__contains___`(which enables `x is in y`), etc. See [example 6.3](https://dabeaz-course.github.io/practical-python/Notes/06_Generators/01_Iteration_protocol.html).

6.2 Customized Generators
----------------
* A generator function creates a generator object, which does NOT immediately execute the function.
  * The generator object only executes on `__next__()` call.
  * You can use a generator to hide a bunch of custom processing in a function and use it to feed a for-loop.
  * Generators can be an interesting way to monitor real-time data sources such as log files or stock market feeds. See [Exercise 6.7](https://dabeaz-course.github.io/practical-python/Notes/06_Generators/02_Customizing_iteration.html).

```python
def countdown(n):
    # Added a print statement
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1

>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10

```


6.3 Producers, Consumers and Pipelines
-----------
```python
{
  # Producer
  def follow(f):
      ...
      while True:
          ...
          yield line        # Produces value in `line` below
          ...

  # Consumer
  for line in follow(f):    # Consumes value from `yield` above
      ...
}
```
`yield` produces values that `for` consumes.

 * You can create various generator functions and chain them together to perform processing involving data-flow pipelines. 
 * In addition, you can create functions that package a series of pipeline stages into a single function call.
  
6.4 More generators
-----------
* The main use of generator expressions is in code that performs some calculation on a sequence, but only uses the result once.
* With generators, the code **runs faster and uses little memory**. It’s like **a filter applied to a stream**.
* A generator expression can only be used **once**.
* `b = (2*x for x in [1,2,3,4])` gives you a generator! Note its difference from list comprehension.

**Advantages of using generators**
* Many problems are much more clearly expressed in terms of iteration.
  * Looping over a collection of items and performing some kind of operation (searching, replacing, modifying, etc.).
  * Processing pipelines can be applied to a wide range of data processing problems.
* Better memory efficiency.
  * Only produce values when needed.
  * Contrast to constructing giant lists.
  * Can operate on streaming data
* Generators encourage code reuse
  * Separates the iteration from code that uses the iteration
  * You can build a toolbox of interesting iteration functions and mix-n-match.

Section 7 Advanced Topics
================
7.1 Variable Arguments
-----------
* A function that accepts **any number of arguments** is said to use **variable arguments**.
  * e.g. `def f(x, *args)`
* A function can also accept any number of **keyword arguments**.
  * e.g. `def f(x, y, **kwargs):`
* To put these two together, we have
```python
{
  def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    ...
}
```
* On the other hand, use * and ** to unpack tuples (into variable arguments) and dictionaries (into keyword arguments), respectively.


7.2 Anonymous Functions and Lambda Functions
-----------
* lambda is highly restricted.
* Only a single expression is allowed.
* No statements like if, while, etc.
* Most common use is with functions like sort().

Lambda can effectively shorten the initial version of code with an extra function:
```python 
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```


7.3 Returning functions
-----------
* Closure functions: A closure retains the values of all variables needed for the function to run properly later on. Common applications:
  * Use in callback functions.
  * Delayed evaluation.
  * Decorator functions.

Exercise [7.7](https://dabeaz-course.github.io/practical-python/Notes/07_Advanced_Topics/03_Returning_functions.html) is very interesting...
* Closures and lambda can often be used to simplify code and eliminate annoying repetition


7.4 Function decorators
-----------
* You can write a **wrapper function** with logging functions.
* Usually, decorators are constructed in response to **repetitive code** appearing across a wide range of function definitions. A decorator can move that code to a central definition.

7.5 Decorator methods
-----------
* `@staticmethod`: used to define a so-called **static class methods** (from C++/Java). A static method is a function that is part of the class, but which **does not operate on instances**.
* `@classmethod`: is used to define class methods. A class method is a method that receives the **class** object as the first parameter instead of the **instance**.

Section 8 Testing and debugging
=======
8.3 Debugging
-----------
* Use **interactive mode** for easier debugging!!
* Use `repr()` when `print` certain variables for debugging!!
* Use the python debugger:
  * `breakpoint()`
  * `bash % python3 -m pdb someprogram.py`