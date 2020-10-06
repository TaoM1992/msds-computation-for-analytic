Practice Test #3
=======

Disclaimer - This practice test might be easier (or more difficult) than the actual test.

The correct answers are in html comments, viewable in the source code.

-----

1) If you read both `brian_spiering` and `USFEmployee` in a code base. Which one is most likely to be the class object?

<!--- 
USFEmployee is most likely the class object. A class models a general category and the identifier is written in CamelCase.

brian_spiering is most likely the instance object. An instance models a specific entity and the identifier is written in snake_case.
--->   


2) What is the single, complete command do you need to type into the terminal to download https://github.com/brianspiering/ml_lab repo for the first time? (Do NOT chain / pipe commands together)

<!--- 
git clone https://github.com/brianspiering/ml_lab

git clone 'https://github.com/brianspiering/ml_lab'

git clone "https://github.com/brianspiering/ml_lab"
--->   
 
3) After running this code, what is the value of the result variable?

```python
func = lambda x: return x//x
result = func(2)
```

<!--- 
Code does not run. It raises a SyntaxError because a lambda function can’t contain the return statement.
--->   

4) As written, the following statement is invalid. What is the smallest change can you make so the statement will be valid.

```python
result = 'a' + 'b'
        + 'c' + 'd'
        + 'e' + 'f'
```

<!--- 
result = ('a' + 'b'
        + 'c' + 'd'
        + 'e' + 'f')

result = 'a' + 'b' \
        + 'c' + 'd' \
        + 'e' + 'f'
--->   

5) Which of the following is the best choice to make sure that a file object is properly closed after it has been used?

a) `f.close()``

b) Use a `with` context manager

c) Use a try/except/finally block

d) Does not matter because Python will always close files automagically

<!--- 
Correct answer:
b) Use a `with` context manager 
--->  