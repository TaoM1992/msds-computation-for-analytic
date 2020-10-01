Command Line Activities
======

In the breakout rooms, each person should individually complete following tasks. The goal is procedural fluency - seeing a prompt and successfully typing in a solution. If you get stuck ask someone else in the breakout rooms to help you. Do all the following tasks locally in a terminal window.

-----
Fundamental Tasks & Commands
-----

The commands to do the following tasks should be memorized. If you have to look-up any of them up, you need to take the time to memorized them. Flashcards are a great tool for memorizing them.

(These might appear on a test as fill in the blank.)

- List the current directory path.
    <!--- $ pwd  --->   
- Navigate to the desktop directory.
    <!--- $ cd ~/Desktop/  --->  
- List the files on your desktop.
    <!--- ls --->   
- List all the files on your desktop, including hidden files.
    <!--- ls -al--->    
- Clear the output from the screen.
    <!--- clear  --->    
- Go through history of command to list the files again.
    <!--- [USE UP ARROW]  --->    
- Look at the help documentation for the `cat` command.
     <!--- man cat  --->   
- From the desktop directory navigate to your GitHub folder for this class. Try to do in a single command.
    <!--- cd ../github/computation_course/  --->   >   
- Find the version of Python you are running.
    <!--- python --version  --->   
- Install `GoogleNews` Python package.
    <!--- pip install GoogleNews ---> 
- Start a Jupyter Notebook or Jupyter Lab server.
    <!--- jupyter notebook --browser=Chrome  --->   
    <!--- jupyter lab --browser=Chrome  --->   
- Stop the currently running Jupyter Notebook or Jupyter Lab server.
    <!--- [CONTROL+C]  ---> 

-------
Common Tasks & Commands
-----

You should be very familiar with the following tasks and commands since they come up often. It strongly suggested you memorized them. 

(These might appear on a test as multiple choice)

- Create a new directory called `temp`.
    <!--- mkdir temp  --->   
- Navigate into that directory.
    <!--- cd temp   ---> 
- Create a new file called `hello.txt`.
    <!--- touch hello.txt  --->   
- Open that file in nano, write `Hello, world!`, save, and exit.
    <!--- nano hello.txt    ---> 
- Display the contents of `hello.txt` on the screen.
    <!--- cat hello.txt    ---> 
- Make copy of `hello.txt` called `hello2.txt`.
    <!--- cp hello.txt hello2.txt    ---> 
- Delete both the folder and all the files in a single command.
    <!--- rm -rf temp  --->   
- Find the full path of the Python interpreter. This makes sure you are running the right copy of Python.
    <!--- which python  --->
- Find all of the pip and conda packages installed.
    <!--- pip list  --->   
    <!--- conda list  --->   
- Install `ponysay` (Brian's favorite command line utility).
     <!--- you may have to install homebrew first  --->  
     <!--- brew install ponysay  --->   
- Then say get a pony to say "It needs to be about 20% cooler."
     <!--- ponysay "It needs to be about 20% cooler." --->   
    