Cools Tools
=====


Where is the stuff for this course?
-----

- GitHub - Store code in the cloud making it easy to share and collaborate. All course materials are code, thus on GitHub.
- Canvas - Learning management system, aka the grade book. Canvas will list when assignments are due and your current grade.


Where can I run Python?
------

- Jupyter Lab / Notebook - De facto integrated development environment (IDE) for Data Scientists.
- [Google Colab](https://colab.research.google.com) - Live Jupyter Notebooks in the browser. Since it is from Google, it is similar to Google Drive. 
- [Deepnote](https://deepnote.com/) - Live Jupyter Notebooks in the browser. If you want a code review, you must send Brian a link to a _private_ example on either repl.it, Google Colab, or Deepnote.
- [repl.it](https://repl.it/) - Coding in the browser in many languages. However, Jupyter Notebooks are currently not supported. 

How can I setup Python and install packages?
------
- Anaconda - A Python distribution made for Data Scientists. Also the name of the company behind the Python distribution.
- pip - Installs Python packages. Can install __any__ package. However, packages may not be optimized for your hardware and may conflict with other package versions.
- conda - Also installs Python packages. Packages have to be on the conda platform in a channel. Packages are optimized for your hardware and are guaranteed not to conflict with other packages. 
    + Rough guidelines:
        * Try to install `numpy` package in a Jupyter Notebook:  
        
            ```
             import sys  
             ! conda install --yes --prefix   {sys.prefix} numpy
             
        * If it doesn't work try - `! pip install numpy`
        - If that doesn't work, ask Brian (even after this class. Brian is always around for programming help.)
    	- Source - [Installing Python Packages from a Jupyter Notebook](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

Optional (but highly recommended)
-----

- [nbviewer](https://nbviewer.jupyter.org/) - View static Jupyter Notebooks in the browser. Better rendering that GitHub. I suggest using [nbviewer extension for Chrome](https://chrome.google.com/webstore/detail/open-in-nbviewer/ihlhlehlibooakiicbiakgojckpnlali?hl=en).
- [nteract](https://nteract.io/) Double click on a local notebook to open it. Game changer.
- [Python Tutor](http://www.pythontutor.com/) - Visualize code execution. The best tool for understanding how Python runs code and works as a visual debugger.
