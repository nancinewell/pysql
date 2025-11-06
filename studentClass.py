import random
import sqlite3

class Student():
    def __init__(self):
        self.getStudents()
        self.resetPlayers()
    
    #list of all students in database
    allStudents = []
    #changing list of players 
    players = [""]
    
    randomPlayer = players[0]

    # return a random student
    def randomPlayerSelection(self):
        #if players is empty, refill it
        if not self.players: self.resetPlayers()
        self.randomPlayer = self.players[0]
        #remove player from list
        del self.players[0]
        #return player
        return self.randomPlayer
          
    #reset players
    def resetPlayers(self):
        self.players = self.allStudents.copy()
        random.shuffle(self.players)

    #add student
    def addStudent(self, name, img):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #insert new monster
        addNewStudent = f"""INSERT INTO students (name, image) 
        VALUES ('{name}', '{img}');"""
        c.execute(addNewStudent)
        #commit & close connection
        conn.commit()
        conn.close()

    #get Students
    def getStudents(self):
        #clear student list
        self.allStudents.clear()
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select all students
        c.execute("SELECT * FROM students")
        fetchedStudents = c.fetchall()
        #add students to the list
        for student in fetchedStudents:
            self.allStudents.append(student)
        #commit & close connection
        conn.commit()
        conn.close()

    #get single student by id
    def getStudent(self, student_id):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select student
        c.execute(f"SELECT * FROM students WHERE student_id = '{student_id}'")
        fetchedStudent = c.fetchone()
        #commit & close connection
        conn.commit()
        conn.close()

        return fetchedStudent

    #modify student
    def updateStudent(self, student_id, name, img):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #modify student
        modifyStudent = f"""UPDATE students SET name = '{name}', image = '{img}'
        WHERE student_id = '{student_id}';"""
        c.execute(modifyStudent)
        #commit & close connection
        conn.commit()
        conn.close()

   
    #delete student
    def deleteStudent(self, student_id):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #delete Student
        removeStudent = f"""DELETE FROM students
        WHERE student_id = '{student_id}';"""
        c.execute(removeStudent)
        #commit & close connection
        conn.commit()
        conn.close()
    
    def openConnection(self):
        conn = sqlite3.connect('bossbattle.db')
        return conn
    