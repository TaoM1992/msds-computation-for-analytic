Practice Test #2
=======

Disclaimer - This practice test might be easier (or more difficult) than the actual test.

The correct answers are in html comments, viewable in the source code.

-----

1) What goes in the blanks to complete this code?

```python
string = 'all that it is'
substring = string[____:____:___] 
assert substring == 'stttl'
```

<!--- 
There are many possible correct answers:

substring = string[-1:0:-3] 
substring = string[-1::-3] 
substring = string[-1:-15:-3] 
substring = string[-1:-14:-3] 
--->   


2) What goes in the blank to complete this code?

```python
def func(s):
    new_string = ""

    for c in s:
        if c.istitle():
            new_string += c.______________()
        else:
            new_string += c.title()
    return new_string

assert swap_case("Www.UsfCA.com") == "wWW.uSFca.COM"
assert swap_case("Pythonist") == "pYTHONIST"
```

<!--- 
lower
--->   


3) After running this code, what is the value of the result variable?

```python
result = len(str(21 * 2)) + "42"
```

<!--- 
TypeError: unsupported operand type(s) for +: 'int' and 'str'
--->   

4) After running this code, what is the value of the result variable?

```python
nums = ([1, 2, 3], [4, 5, 6]) 
nums[0][2] = 0
result = nums
```

<!---  
([1, 2, 0], [4, 5, 6]) 
--->   

5) After running this code, what is the value of the result variable?

```python
results = {'b', 'a', 'z'}.difference('abc') 
```

<!--- 
'z'
--->   

6) Strings share the fewest methods with which of the following other data structures:

a) lists  
b) tuples  
c) sets    


<!--- 
The correct answer is: c) sets

Strings are sequenced collections, similar to lists and tuples.

Sets are unordered collections.
--->   

7) Which of the following is false?

a) A dictionary maps a keys to a specific value.    
b) A dictionary’s keys must be mutable and unique.     
c) Multiple keys can have the same value.   


<!--- 
The correct answer is: b) A dictionary’s keys must be mutable and unique. 

A dictionary’s keys must be IMMUTABLE.  
They also have to be unique.
--->   
