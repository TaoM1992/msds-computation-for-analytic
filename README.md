<center><h2>Computation for Analytics <br> University of San Francisco's MSDS 501 Fall 2020</h2></center>

<center><img src="https://imgs.xkcd.com/comics/python.png" style="width: 40%"/></center>

----
Course Description
----

This course is part of the [MS in Data Science program at the University of San Francisco](https://www.usfca.edu/arts-sciences/graduate-programs/data-science) and is specifically designed as a catalyst to improve computer programming skills for those who are not yet skilled programmers. The course will focus on the applied computer programming concepts and skills directly related to data science.

Writing software is about problem-solving, data structures, algorithms, computer languages, libraries, software tools, and computing devices. In this course, I'm going to teach you how to approach programming, review the key elements of Python, teach you how to leverage Python to solve data science problems, introduce you to the command line, and finally introduce you to cloud computing. You'll go deeper into fundamental data structures and algorithms later in the MSDS program in courses that specifically cover those topics.

----
Logistics
----

__Instructor:__ Brian Spiering   
__Contact__: Slack - [@Brian Spiering](https://msan-usf.slack.com/messages/DAMAXHTL5) (more preferred) | Email - [bspiering@usfca.edu](mailto:bspiering@usfca.edu) (less preferred)  
__Office hours__: Mondays 5-6p (PDT) and Tuesdays 9-10a (PDT). And by appointment. Zoom link in Slack channel.

__Grader__: Nishat Parveen   
__Contact__: Slack - [@Nishat](https://msan-usf.slack.com/archives/DMSH3QPHR) | Email - [nparveenmehboobkhan@usfca.edu](mailto:nparveenmehboobkhan@usfca.edu) 

__Website__: [github.com/brianspiering/
computation_course](https://github.com/brianspiering/computation_course)    
__Communication__: Slack [`#computation_course_2020`](https://msan-usf.slack.com/archives/C0192004FGR)  
__Location__: Zoom (see link in course calendar, Canvas, or in Slack)   

__Sections__:

1 - Mondays*  and Wednesday* from  1:00p -  1:50p (PDT)   
2 - Mondays*  and Wednesday* from  2:00p -  2:50p (PDT)  
3 - Mondays*  and Wednesday* from  4:00p -  4:50p (PDT)  
5a - Mondays*  and Wednesday* from  7:00p -  7:50p (PDT)  
5b - Tuesdays* and Thursdays* from 10:00a - 10:50a (PDT)  

\* Except first week. Due to orientation, each class will be shifted one day forward (e.g., Monday ⇨ Tuesday)

Anyone enrolled in the MSDS program can audit the course. You do __not__ need my permission or notify me if you want to audit. Just show up! All course materials are in GitHub. Canvas is only for grading thus available only to enrolled students. All the course materials are autograded so you can try the exercises and see where you stand.

Feel free to attend the section that works best for your schedule. Each section will cover the same material.

Prerequisites
----

- Acceptance into the MSDS program.

Learning Outcomes
----

By the end of the course, you should be able to:  

1. Write Python code to solve data-related problems.
1. Define common programming terms in your own words.
1. Fluently use the Python console, Jupyter Notebook environment, and Python scripts to write, test, and debug Python code.
1. Read and use programming language documentation.
1. Use the fundamental features of the Unix command line, git, and GitHub.

----
Course Schedule and Topics (Tentative)
----

01. 08/18 Tuesday / Wednesday
    - Welcome 
    - Overview of course
02. 08/20 Thursday / Friday
    - Introduction to Python
    - Variables
    - Numeric Types
    - Strings
03. 08/24 Monday / Tuesday
    - Comparison Operators: ==, !=, is
    - Control Statements: if, elif, else
04. 08/26 Wednesday
    - Looping: for, while
    - Booleans: and, or, not
05. 08/31 Monday / Tuesday
    - User defined functions
    - Standard Library
    - Keyword arguments
06. 09/02 Wednesday / Thursday
    - Methods
    - Scope rules
    - Recursion
07. 09/07 Monday / Tuesday
    - Lists
    - Tuples
    - Slicing
08. 09/09  Wednesday / Thursday
    - List methods
    - List comprehensions
09. 09/14 Monday / Tuesday
    - Generator expressions
    - Filter, map, and reduce
10. 09/16  Wednesday / Thursday
    - Dictionaries
    - Sets
11. 09/21 Monday / Tuesday
    - Strings
    - String formatting
12. 09/23  Wednesday / Thursday
    - File handling
13. 09/28 Monday / Tuesday
    - User defined classes
14. 09/30 Wednesday 
    - Command line
15. 10/05 Monday / Tuesday
    - git / GitHub
16. 10/07 Wednesday / Thursday
    - Amazon Web Services (AWS)

Topics Not Covered
-----

- Introduction to programming (the course assumes you already know the very basics of programming)
- Implementation of fundamental programming data structures (e.g., linked lists) and algorithms (e.g., sorting)
- Python 2 and R programming language
- Other libraries in Python's data science stack: NumPy, SciPy, scikit-learn, Pandas
- Advanced OOP: Multiple inheritance, static methods, property methods
- Dynamic programming  
- Data visualization 
- Concurrency, threading, `async` module
- Distributed computing

----
Grading
----

| Item           | Weight   | Due Date & Time                  |
|:---------------|:--------:|:---------------------------------|
| Professionalism| 14%      | All the time                     |
| Prework Check  | 15%      | Before each class                |
| Setup          |  1%      | 08/21 Friday 5p PDT              |
| Homework 1     | 10%      | 08/26 Wednesday 1p PDT           |
| Homework 2     | 10%      | 09/02 Wednesday 1p PDT           |
| Test 1         | 10%      | 09/09 Wednesday 8-9a or 8-9p PDT |
| Homework 3     | 10%      | 09/16 Wednesday 1p PDT           |
| Test 2         | 10%      | 09/23 Wednesday 8-9a or 8-9p PDT |
| Homework 4     | 10%      | 09/30 Wednesday 1p PDT           |
| Test 3         | 10%      | 10/07 Wednesday 8-9a or 8-9p PDT |
| __Total__      | __100%__ |

Each item's contribution is capped its respective percentage. The total course percentage is capped at 100%.

Currently, there is no extra credit. If there is any extra credit, it is entirely at the discretion of the instructor.

We'll be using Canvas as the learning management system (LMS), aka the gradebook. The instructional team will do their best to have Canvas accurately reflect your current scores in the course. However, Canvas may not be completely accurate all the time. In other words, your actual grade maybe significant different than it appears on Canvas. 

### Professionalism

I expect you act professionally at all times: in-person and electronically; during class outside class. Since people come up from a variety of backgrounds, I'm explicitly defining professionalism: 

- Show up on time and prepared.
- Remain fully present.
- Contribute appropriately and meaningfully.
- Follow staff and faculty instructions appropriately.
- Show respect to all people.

Professionalism points are entirely at the instructor's discretion. 

Violations of Academic Integrity are unprofessional, thus you'll automatically lose all Professionalism points for any violations of Academic Integrity. 

Tardiness negatively impacts an active learning environment, thus will impact your professionalism grade.

You must show-up to each session prepared. Each person is important to the dynamic of the class, and therefore students are required to participate in class activities. Expect to be "cold called". I call on students at random not to put you on the spot but to keep you engaged in the material at all times.

I expect you to be fully present and engaged in the classroom at all times. I _strongly_ suggest taking notes on paper.

I except you follow the [etiquette guidelines](https://github.com/brianspiering/teaching_materials/blob/master/online_class_etiquette_guidelines.md) throughout the entire course. This is your warning. Every violation will result in a loss of participation points, negatively impacting your total grade. 

### Prework Check 

There will be a required prework __before__ each class. The prework will check that you have watch the videos, read the reading, and are prepared for the in-class activities. The prework check also allows me to get a sense for the current understanding of the class. I know which material I can skim/skip and which material to over in greater detail.

The prework will be online in Canvas.

### Setup 

Completing the MSDS Student Info Survey and setting up online profiles for the tools MSDS program uses.

### Homework

Each homework will be a collection of coding problems in Python. 

Late assignments will only be accepted for medical emergencies.

Asking for acceptance of any late assignments without a medical emergency or submitting assignment not through GitHub Classroom will result in a loss of professionalism points (and your assignment will still not be accepted).

### Tests

Tests will be a combination of multiple choice, short answer, and programming questions.

Missing tests will only be accommodated for medical emergencies.

More detailed information is in the test policies document in the resources folder on the course website.

Grading standards
----

The MSDS program considers a grade of "A" to represent exceptional work with respect to both the instructor's expectations and peer student achievements. I consider an "A" grade to be above and beyond what most students achieve. A grade of "B" represents the expected outcome, what is called "competence" in a business setting. A "C" grade represents achievements lower than the instructor's expectations for competence in the subject. A grade of "F" represents little or no work in the course.

I have the right, but not the obligation, to "curve" the final numerical grades at the end of the course. The mapping from percentages to letter grades (e.g., [95, 100] is an A, [90,95) is an A-, etc.) will not be established until the end of the course. Roughly, the top 15% of students will receive grades of A or A-. Roughly, 60% of students will receive grades of B+, B, or B-. Roughly, 20% of students will receive grades of C+, C, or C-. Students can receive failing grades. I am not required by program to fail a particular percentage of students, but I will fail students if it is appropriate. Students who fail this course __cannot__ continue in the MSDS program. 

Students with disabilities
-----

If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact [USF Student Disability Services](https://myusf.usfca.edu/sds) (SDS) for information about accommodations.

Behavioral Expectations
----

All students are expected to behave in accordance with the [Student Conduct Code](https://myusf.usfca.edu/fogcutter) and other University policies.

Academic Integrity
-----

USF upholds the standards of honesty and integrity from all members of the academic community. All students are expected to know and adhere to the University's [Honor Code](https://myusf.usfca.edu/academic-integrity/).

You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action. Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation. You must also abide by the copyright laws of the United States.

The golden rule: **You must never represent another person’s work as your own.** Credit to [Terence Parr](https://github.com/parrt/msds689).

I generously post all my materials to a public GitHub repo. However, you should not post any solutions to GitHub (or anywhere else on the Internet). __Publicly posting any solutions to any problems for this course will result in a failing grade for this course.__

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

Counseling and Psychological Services (CAPS)
-----

CAPS provides confidential, free [counseling](https://myusf.usfca.edu/student-health-safety/caps) to student members of our community.

Confidentiality, Mandatory Reporting, and Sexual Assault
-------

For information and resources regarding sexual misconduct or assault visit the [Title IX](https://myusf.usfca.edu/TITLE-IX) coordinator or USF's [Callisto website](http://usfca.callistocampus.org/).
