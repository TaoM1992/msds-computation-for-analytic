Comment style guidelines
=======

__In this course, every line of code you write should have a comment.__

Syntax Guidelines
------

- There will always be a space after the `#`.  
- It is preferred if the first word is title cased. All lower case is acceptable. 
- Period is optional.
- If commenting several related lines, align the comments away from the code so the code and comments can be read more easily.

Examples
-------

```python
# The meaning of everything.
x = 42 

today = "Tuesday" # The current day of the week

def my_mean(nums: Sequence[float]) -> float:
    "Calculate the arithmetic mean, similar to built-in sum"
    total, count = 0, 0   # Initialize values
    
    for n in nums:        # Step through each input value
        total += n        # Use accumulator pattern to update running total
        count += 1        # Use accumulator pattern to update counter
    
    return total / count  # Arithmetic mean is sum of values over number of values

```

What should be in a comment?
------

- A comment adds additional information beyond the code.   
- A comment describes the why (vs the what).   
- A comment is complete thought. 

But pep8 says something different about requiring comments…
------

[pep8](https://pep8.org/) is a general style guidelines. Different places can have different style guidelines. Our style guidelines require a comment for each line of you write.

Every line should have a comment for the following reasons:

1. It encourages you to write only meaningful lines of code. You should clear code in the fewest lines possible.
2. It encourages to you think about your code. The act of explaining the logic behind your code will help you improve as a programmer.
4. It encourages of academic integrity. Much of the code is in the course will look similar across people. However, the comments should be very different across people.
