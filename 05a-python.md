# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A tuple is a sequence of values of any type and is indexed by an integer making it similar to a list. Tuples and lists can both contain duplicate elements and slicing can be done. A tuple differs from a list in that it is immutable, meaning you can't modify the elements within it; however, one tuple can be replaced with another tuple. Because a list is mutable it cannot be used as a key in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lits are both mutable; however, sets store unordered values and do not have an index associated with them. Unlike lists, sets are unordered and have no duplicate data. Generally, because sets use hashing, finding an element in large sets is faster.


---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are small anonymous (i.e., without a name) functions that take any number of arguments but only a single expression. These functions can be used wherever an object is required. Lambda functions are used when a name less function is necessary for a short period of time. Below is an example of using the `lambda` function as the `key` argument in `sorted`. This example sorts even-numbered words after odd-numbered words.

`new_list = ['i', 'am', 'the', 'best', 'of', 'all', 'time', 'forever', 'sheep', 'infinity']  
print(sorted(new_list, key = lambda word: len(word) %2 == 0))  
['i', 'the', 'all', 'forever', 'sheep', 'am', 'best', 'of', 'time', 'infinity']`

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a simpler way to create lists where each element is the result of an operation. List comprehensions are usually faster than for loops, but they are more difficult to debug.

**List Comprehension/Map Example**
*List Comprehension*
`squares = [x**2 for x in range(10)]
print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

*Map*
`squares = [i for i in map(lambda x: x**2, range(10))]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

**List Comprehension/Filter Example**
*List Comprehension*
`def f(x):
  return x % 2 == 0
evens = [x for x in range(25) if f(x)]
print(evens)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]`
  
*Filter*
`def f(x):
  return x % 2 == 0 
evens = filter(f, range(25))
list(evens)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]`

>> Maps and filters both return list objects similar to a list comprehension. Maps, like list comprehensions, apply functions over iterables. Filters are similar to maps, and adds to the list any element for which the boolen returned true.

**Set Comprehension Example**

`set_comp = {x**2 for x in range(25)}
set_comp
{0, 1, 256, 4, 9, 16, 144, 400, 529, 25, 289, 36, 169, 49, 441, 64, 576, 196, 324, 81, 225, 100, 484, 361, 121}`

**Dictionary Comprehension Example**

`dict_comp = {x: x**2 for x in range(25)}
dict_comp
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576}`

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





