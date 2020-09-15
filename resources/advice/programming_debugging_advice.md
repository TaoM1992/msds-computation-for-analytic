What to do when your code doesn't work
======

If you have problems, follow these steps:

1. Don't Panic! Relax and realize that you will solve this problem, even if it takes a little bit of messing around. Banging your head against the computer is part of your job. Remember that the computer is doing precisely what you tell it to do. There is no mystery.

1. Determine precisely what is going on. Did you get an error message from Python?  Is it a syntax error? If so, review the syntax of all your statements and expressions.  

2. If you got an error message that has what we call a stack trace, a number of things could be wrong. You read a stack trace from bottom-to-top. Go slowly and understand each character and each line.

    Given this stack track:

    ```
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-39-86d19b3216b2> in <module>()
          1 from PIL import Image
          2 
    ----> 3 image = Image.opem('eye.png')
          4 image = image.convert("L") # grayscale
          5 image

    AttributeError: module 'PIL.Image' has no attribute 'opem'
    ```
    
    I simply misspelled `open()` as `opem()`.

1. If it does not look like it some simple misspelling, you might get lucky and find something in Google if you cut-and-paste that error message.

1. If your code is at least running and doing something, then insert print statements to figure out what the variables are and how far into the program you get before a craps out. That often tells you what the problem is. Something like `print(f"Expected {foo}. But got {bar}.")`

1. Definitely try to solve the problem yourself, but don't waste too much time (~15 minutes at the upper end). I can typically help you out quickly so you can move forward.

[Source](https://github.com/parrt/msds501/blob/master/projects/images.pdf)

[Terence Parr's The Essentials Of Debugging](https://blog.parr.us/2014/11/17/the-essentials-of-debugging/)
