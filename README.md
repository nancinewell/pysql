# Overview
I just spent a few weeks learning about Python and wanted to take it a step further by incorporating a database. In my learning, I found that SQLite3 is natively supported in Python, so I wanted to explore the possibilities there. 

This program is a database of questions with answers, added, modified, and deleted by the teacher as needed, that will be displayed to students. There is also a table of students, and a table of monsters. Monsters are assigned to a "bank" of questions that will be used in the future when the boss battle is actually active. 

This program, like most things I write as I'm learning, is meant to enhance my homeschool. It will eventually run a "Boss Battle" (which is just a gamified quiz to help the kids get excited about reviews), displaying questions, then answers (after the student provides their answer).

[Software Demo Video](https://youtu.be/7Num9L445Oc)

# Relational Database
I used SQLite3, as it is supported in Python by simply importing the appropriate library. It doesn't require a separate server, making it easy to work with. It works very similar to SQL, but is limited to the most commonly used features and commands. The source code is in the public domain, making it free for everyone to use.

Tables:
    Students (student_id, name, image)
    Monsters (monster_id, name, image, bank)
    Questions (question_id, question, answer, bank)

Monsters and Questions both have a "bank" field, so the teacher can assign monster(s) to a question bank. When the boss battle starts, it will select a random monster assigned to the question bank being used. 

A student will be assigned randomly to each question until all students have answered. Then the students will be shuffled and presented one at a time again as needed until all questions are answered, or the monster is defeated.


# Development Environment
I wrote this program in the IDE Visual Studio Code version 1.105.1 with 4 extensions to make it more friendly to Python: Pylance, Python, Python Debugger, and Python Environments.

I wrote this program using Python with Tkinter for the front end and SQLite3 for the database.

# Useful Websites
- [ActiveState Academy](https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/)
- [SQLite Databases with Python - Full Course](https://www.youtube.com/watch?v=byHcYRpMgI4)
- [Geeks for Geeks](https://www.geeksforgeeks.org/category/python/)
- [Tkinter](https://tkinter.com/scrollable-frames-tkinter-customtkinter-8/)
- [Sololearn](https://www.sololearn.com)
- [SQLITE Tutorial](https://www.sqlitetutorial.net/)
- [Python](https://docs.python.org/3.8/library/sqlite3.html)
- [DigitalOcean](https://www.digitalocean.com/community/tutorials/python-remove-duplicates-from-list)
- [W3Schools](https://www.w3schools.com/sql)

# Future Work
- I would like to make the Image field a drop down to make it more user friendly- choose from a list of images instead of typing it out and hoping it's correct.
- I would like to learn another front-end method for Python. Tkinter gets the job done, but it's not customizable enough for modern applications to have a modern look and feel.
- I would like to refactor the code to break out the massive amount of functions in WhatToDo(). I would like to break it out by Access Students, Access Monsters, Access Questions, and Boss Battle.