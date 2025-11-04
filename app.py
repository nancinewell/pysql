import sqlite3
import tkinter as tk
import customtkinter as ctk
from monsterClass import Monster 
from studentClass import Student
from questionsClass import Question
from PIL import ImageTk, Image  

# # # # # # # # # # #  CREATE TABLES  # # # # # # # # # #
#define connection and cursor
conn = sqlite3.connect('bossbattle.db')
c = conn.cursor()

#create monster table
createMosterTable = """CREATE TABLE IF NOT EXISTS
monsters(
monster_id INTEGER PRIMARY KEY
, name TEXT
, image TEXT)
"""
c.execute(createMosterTable)

#create student table
createStudentTable = """CREATE TABLE IF NOT EXISTS
students(
student_id INTEGER PRIMARY KEY
, name TEXT
, image TEXT)"""
c.execute(createStudentTable)

#create questions table
createQuestionTable = """CREATE TABLE IF NOT EXISTS
questions(
question_id INTEGER PRIMARY KEY
, question TEXT
, answer TEXT
, bank TEXT)"""
c.execute(createQuestionTable)

#commit to database
conn.commit()

#close connection
conn.close()

# # # # # # # # # # #  GLOBALS  # # # # # # # # # #
#Instantiate monster and players
wanderingMonster = Monster()

students = Student()

questions = Question()

# # # # # # # # # # # # # # # # MAIN FUNCTION # # # # # # # # # # # # # # # # 
def main():
    app = Application()
    app.mainloop()

# # # # # # # # # # # # # # # # APPLICATION # # # # # # # # # # # # # # # # 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #set app title
        self.title("Boss Battle")
        #set size of app
        self.geometry('700x500')

        #set frame configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)        

        #run the next piece in the frame
        frame1 = WhatToDo(self)
        frame1.grid(row = 0, column = 0, sticky="news", padx = 15, pady = 15)

class WhatToDo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #configure rows/columns
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.WelcomeOptions()
      
    def WelcomeOptions(self, frame = None,  msg = None):
        #Destroy previous frame if necessary
        self.destroyThing(frame)
        #Create new frame for content
        self.welcomeFrame = tk.Frame(self)
        self.welcomeFrame.grid(row = 0, column = 0)
        #if a message was passed, display it.
        if msg: 
            self.msgLabel = tk.Label(self.welcomeFrame, text = msg, font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "blue")
            self.msgLabel.grid(row = 0, column = 0, sticky="ew")
        #welcome question 
        self.welcomeLabel = tk.Label(self.welcomeFrame, text = "What would you like to do?", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.welcomeLabel.grid(row = 1, column = 0, pady = 5)
 
        #Option Buttons
        self.bossBattleBtn = tk.Button(self.welcomeFrame, text = "Boss Battle!", font = ("Times New Roman", 14), command = lambda: self.BBSetup(self.welcomeFrame)) 
        self.bossBattleBtn.grid(row = 2, column = 0, pady = 10)

        self.studentBtn = tk.Button(self.welcomeFrame, text = "Access Students", font = ("Times New Roman", 14), command = lambda: self.AccessStudents(self.welcomeFrame)) 
        self.studentBtn.grid(row = 3, column = 0, pady = 10)

        self.monsterBtn = tk.Button(self.welcomeFrame, text = "Access Monsters", font = ("Times New Roman", 14), command = lambda:self.AccessMonsters(self.welcomeFrame)) 
        self.monsterBtn.grid(row = 4, column = 0, pady = 10)
        
        self.questionBtn = tk.Button(self.welcomeFrame, text = "Access Questions", font = ("Times New Roman", 14), command = lambda:self.AccessQuestions(self.welcomeFrame)) 
        self.questionBtn.grid(row = 5, column = 0, pady = 10)

# # # # # # # # # # # # # # # # # # # # # # # # # image testing # # # # # # # # # # # # # # # # # # # # # # # # # 
        monsterName = "monster-2.png"
        image1 = ImageTk.PhotoImage(Image.open(f"img/{monsterName}").resize((100,100)))
        label1 = tk.Label(self.welcomeFrame, image=image1)
        label1.image = image1
        label1.grid(row = 6, column = 0)
    
    # # # # # # # # # # #  ACCESS STUDENTS  # # # # # # # # # #
    def AccessStudents(self, frame):
        self.destroyThing(frame)

        self.studentFrame = tk.Frame(self)
        self.studentFrame.grid(row = 0, column = 0)

        #welcome question 
        self.studentAccessLabel = tk.Label(self.studentFrame, text = "What would like to do?", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.studentAccessLabel.grid(row = 0, column = 0, pady = 5)
 
        #Option Buttons
        self.viewStudentsBtn = tk.Button(self.studentFrame, text = "View All Students", font = ("Times New Roman", 14), command = lambda: self.ViewAllStudents(self.studentFrame)) 
        self.viewStudentsBtn.grid(row = 1, column = 0, pady = 10)

        self.addStudentBtn = tk.Button(self.studentFrame, text = "Add a Student", font = ("Times New Roman", 14), command = self.AddStudentForm) 
        self.addStudentBtn.grid(row = 2, column = 0, pady = 10)

        #home button
        self.homeBtn = tk.Button(self.studentFrame, text = "Home", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(frame=self.studentFrame)) 
        self.homeBtn.grid(row = 3, column = 0, pady = 5)  


    def ViewAllStudents(self, frame):
        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.viewAllStudentsFrame = ctk.CTkScrollableFrame(self, fg_color= "gray95")
        self.viewAllStudentsFrame.grid(row = 0, column = 0, sticky = "nsew")
        #configure columns/rows
        self.viewAllStudentsFrame.columnconfigure(0, weight=1)
        self.viewAllStudentsFrame.columnconfigure(1, weight=3)
        self.viewAllStudentsFrame.columnconfigure(2, weight=3)
        self.viewAllStudentsFrame.columnconfigure(3, weight=2)
        self.viewAllStudentsFrame.columnconfigure(4, weight=2)
        self.viewAllStudentsFrame.rowconfigure(0, weight=1)

        #hold headers to send for display
        headers = ["ID", "Name", "Image"]
        #hold students in list to send for display
        students.getStudents()
        getStudents = students.allStudents
        #send list for display
        self.displayList(getStudents, headers, self.viewAllStudentsFrame, "students")     
        #home button
        self.homeBtn = tk.Button(self.viewAllStudentsFrame, text = "Home", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(frame=self.viewAllStudentsFrame)) 
        self.homeBtn.grid(row = 0, column = 4, pady = 5)  
        #scrollbar
        
    
    def AddStudentForm(self):
        #Destroy the previous frame
        self.destroyThing(self.studentFrame)
        #New frame for this page
        self.addStudentFormFrame = tk.Frame(self)
        self.addStudentFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.addStudentFormFrame.columnconfigure(0, weight=1)
        self.addStudentFormFrame.rowconfigure(0, weight=1)   
        #create elements to collect data
        self.addStudentNameLabel = tk.Label(self.addStudentFormFrame, text = "Student Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addStudentNameLabel.grid(row = 0, column = 0)

        self.addStudentNameEntry = tk.Entry(self.addStudentFormFrame, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addStudentNameEntry.grid(row = 1, column = 0)

        self.addStudentImgLabel = tk.Label(self.addStudentFormFrame, text = "Image Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addStudentImgLabel.grid(row = 2, column = 0)

        self.addStudentImgEntry = tk.Entry(self.addStudentFormFrame, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addStudentImgEntry.grid(row = 3, column = 0)
        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.addStudentFormFrame)
        self.BtnFrame.grid(row = 4, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)
        #button to add student
        self.addStudentBtn = tk.Button(self.BtnFrame, text = "Add Student", font = ("Times New Roman", 14), command = lambda: self.AddStudent(self.addStudentNameEntry.get(),self.addStudentImgEntry.get(),self.addStudentFormFrame )) 
        self.addStudentBtn.grid(row = 0, column = 0, pady = 5, padx = 10)

        #button to cancel
        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllQuestions(self.addStudentFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 2, pady = 5, padx = 10) 

    def AddStudent(self, name, img, frame):
        try:
            #add the student with given info
            students.addStudent(name, img)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Student added: {name}")
        except Exception as e:
            #alert user to error message and incomplete addition of student.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Student not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
        

    def EditStudentForm(self, student_id, frame):
        #fetch student
        studentToEdit = students.getStudent(student_id)
        #convert student info to TKString for default values
        studentName = tk.StringVar(value = studentToEdit[1])
        studentImg = tk.StringVar(value = studentToEdit[2])

        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.editStudentFormFrame = tk.Frame(self)
        self.editStudentFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.editStudentFormFrame.columnconfigure(0, weight=1)
        self.editStudentFormFrame.rowconfigure(0, weight=1)   
                
        #create elements to collect data
        self.editStudentNameLabel = tk.Label(self.editStudentFormFrame, text = "Student Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editStudentNameLabel.grid(row = 0, column = 0)

        self.editStudentNameEntry = tk.Entry(self.editStudentFormFrame, textvariable= studentName, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editStudentNameEntry.grid(row = 1, column = 0)

        self.editStudentImgLabel = tk.Label(self.editStudentFormFrame, text = "Image Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editStudentImgLabel.grid(row = 2, column = 0)

        self.editStudentImgEntry = tk.Entry(self.editStudentFormFrame, textvariable= studentImg, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editStudentImgEntry.grid(row = 3, column = 0)

        #try to display avatar
        try:
            studentAvatar = ImageTk.PhotoImage(Image.open(f"img/{studentToEdit[2]}").resize((150,150)))
            self.imageLabel = tk.Label(self.editStudentFormFrame, image=studentAvatar)
            self.imageLabel.image = studentAvatar
            self.imageLabel.grid(row = 4, column = 0, pady = 5)
        finally:
            #create frame to hold buttons
            self.BtnFrame = tk.Frame(self.editStudentFormFrame)
            self.BtnFrame.grid(row = 5, column = 0)
            self.BtnFrame.columnconfigure(0, weight=1) 
            self.BtnFrame.columnconfigure(1, weight=1) 
            self.BtnFrame.columnconfigure(2, weight=1)
            #button to submit updates
            self.editStudentBtn = tk.Button(self.BtnFrame, text = "Update Student", font = ("Times New Roman", 14), command = lambda: self.EditStudent(student_id, self.editStudentNameEntry.get(),self.editStudentImgEntry.get(),self.editStudentFormFrame )) 
            self.editStudentBtn.grid(row = 0, column = 0, pady = 5, padx = 10)

            #button to cancel
            self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllStudents(self.editStudentFormFrame)) 
            self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 
        

    def EditStudent(self, id, name, img, frame):
        try:
            #add the student with given info
            students.updateStudent(id, name, img)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Student updated: {name}")
        except Exception as e:
            #alert user to error message and incomplete addition of student.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Student not updated.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
       
    def DeleteStudentForm(self, student_id, frame):
        #fetch student
        studentToDelete = students.getStudent(student_id)
        print(f"Student fetched: {studentToDelete}")
        #convert student info to TKString for default values
        studentName = studentToDelete[1]
        studentImg = studentToDelete[2]

        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.deleteStudentFormFrame = tk.Frame(self)
        self.deleteStudentFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.deleteStudentFormFrame.columnconfigure(0, weight=1)
        self.deleteStudentFormFrame.rowconfigure(0, weight=1)   
        #display confirmation msg
        self.deleteStudentCfrmLabel = tk.Label(self.deleteStudentFormFrame, text = "Are you sure you want to delete this student?", font= ("Times New Roman", 18), wraplength=350, pady = 15, fg = "red")
        self.deleteStudentCfrmLabel.grid(row = 0, column = 0)
        #display student info
        self.deleteStudentNameLabel = tk.Label(self.deleteStudentFormFrame, text = f"Student Name: {studentName}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteStudentNameLabel.grid(row = 1, column = 0)

        self.deleteStudentImgLabel = tk.Label(self.deleteStudentFormFrame, text = f"Student Image: {studentImg}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteStudentImgLabel.grid(row = 2, column = 0)
        
        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.deleteStudentFormFrame)
        self.BtnFrame.grid(row = 3, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)
        
        #button to confirm deletion
        self.deleteStudentBtn = tk.Button(self.BtnFrame, text = "Delete Student", font = ("Times New Roman", 14), command = lambda: self.DeleteStudent(student_id,self.deleteStudentFormFrame )) 
        self.deleteStudentBtn.grid(row = 0, column = 0, pady = 5, padx = 10)
        #button to cancel
        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllStudents(self.deleteStudentFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 

    def DeleteStudent(self, student_id, frame):
        print(f"DeleteStudent() reached. student_id: {student_id}" )
        try:
            #add the student with given info
            students.deleteStudent(student_id)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Student deleted")
        except Exception as e:
            #alert user to error message and incomplete addition of student.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Student not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
    
    # # # # # # # # # # #  ACCESS MONSTERS  # # # # # # # # # #

    def AccessMonsters(self, frame):
        self.destroyThing(frame)

        self.monsterFrame = tk.Frame(self)
        self.monsterFrame.grid(row = 0, column = 0)

        #welcome question 
        self.monsterAccessLabel = tk.Label(self.monsterFrame, text = "What would like to do?", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.monsterAccessLabel.grid(row = 0, column = 0, pady = 5)
 
        #Option Buttons
        self.viewMonstersBtn = tk.Button(self.monsterFrame, text = "View All Monsters", font = ("Times New Roman", 14), command = lambda: self.ViewAllMonsters(self.monsterFrame)) 
        self.viewMonstersBtn.grid(row = 1, column = 0, pady = 10)

        self.addMonsterBtn = tk.Button(self.monsterFrame, text = "Add a Monster", font = ("Times New Roman", 14), command = self.AddMonsterForm) 
        self.addMonsterBtn.grid(row = 2, column = 0, pady = 10)

        self.homeBtn = tk.Button(self.monsterFrame, text = "Home", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(frame=self.monsterFrame)) 
        self.homeBtn.grid(row = 3, column = 0, pady = 5) 

    def ViewAllMonsters(self, frame):
        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.viewAllMonstersFrame = ctk.CTkScrollableFrame(self, fg_color= "gray95")
        self.viewAllMonstersFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.viewAllMonstersFrame.columnconfigure(0, weight=1)
        self.viewAllMonstersFrame.columnconfigure(1, weight=3)
        self.viewAllMonstersFrame.columnconfigure(2, weight=3)
        self.viewAllMonstersFrame.columnconfigure(3, weight=2)
        self.viewAllMonstersFrame.columnconfigure(4, weight=2)
        self.viewAllMonstersFrame.rowconfigure(0, weight=1)

        #hold headers to send for display
        headers = ["ID", "Name", "Image"]
        #hold monsters in list to send for display
        wanderingMonster.getMonsters()
        getMonsters = wanderingMonster.allMonsters
        #send list for display
        self.displayList(getMonsters, headers, self.viewAllMonstersFrame, "monsters")   

        self.homeBtn = tk.Button(self.viewAllMonstersFrame, text = "Home", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(frame=self.viewAllMonstersFrame)) 
        self.homeBtn.grid(row = 0, column = 4, pady = 5)        
    
    def AddMonsterForm(self):
        #Destroy the previous frame
        self.destroyThing(self.monsterFrame)
        #New frame for this page
        self.addMonsterFormFrame = tk.Frame(self)
        self.addMonsterFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.addMonsterFormFrame.columnconfigure(0, weight=1)
        self.addMonsterFormFrame.rowconfigure(0, weight=1)   
        #create elements to collect data
        self.addMonsterNameLabel = tk.Label(self.addMonsterFormFrame, text = "Monster Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addMonsterNameLabel.grid(row = 0, column = 0)

        self.addMonsterNameEntry = tk.Entry(self.addMonsterFormFrame, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addMonsterNameEntry.grid(row = 1, column = 0)

        self.addMonsterImgLabel = tk.Label(self.addMonsterFormFrame, text = "Image Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addMonsterImgLabel.grid(row = 2, column = 0)

        self.addMonsterImgEntry = tk.Entry(self.addMonsterFormFrame, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addMonsterImgEntry.grid(row = 3, column = 0)

        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.addMonsterFormFrame)
        self.BtnFrame.grid(row = 4, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)

        self.addMonsterBtn = tk.Button(self.BtnFrame, text = "Add Monster", font = ("Times New Roman", 14), command = lambda: self.AddMonster(self.addMonsterNameEntry.get(),self.addMonsterImgEntry.get(),self.addMonsterFormFrame )) 
        self.addMonsterBtn.grid(row = 0, column = 0, pady = 5, padx = 10)

        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllMonsters(self.addMonsterFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 

    def AddMonster(self, name, img, frame):
        try:
            #add the monster with given info
            wanderingMonster.addMonster(name, img)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Monster added: {name}")
        except Exception as e:
            #alert user to error message and incomplete addition of monster.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Monster not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
        
    def EditMonsterForm(self, monster_id, frame):
        #fetch monster
        monsterToEdit = wanderingMonster.getMonster(monster_id)
        #convert monster info to TKString for default values
        monsterName = tk.StringVar(value = monsterToEdit[1])
        monsterImg = tk.StringVar(value = monsterToEdit[2])

        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.editMonsterFormFrame = tk.Frame(self)
        self.editMonsterFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.editMonsterFormFrame.columnconfigure(0, weight=1)
        self.editMonsterFormFrame.rowconfigure(0, weight=1)   
                
        #create elements to collect data
        self.editMonsterNameLabel = tk.Label(self.editMonsterFormFrame, text = "Monster Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editMonsterNameLabel.grid(row = 0, column = 0)

        self.editMonsterNameEntry = tk.Entry(self.editMonsterFormFrame, textvariable= monsterName, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editMonsterNameEntry.grid(row = 1, column = 0)

        self.editMonsterImgLabel = tk.Label(self.editMonsterFormFrame, text = "Image Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editMonsterImgLabel.grid(row = 2, column = 0)

        self.editMonsterImgEntry = tk.Entry(self.editMonsterFormFrame, textvariable= monsterImg, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editMonsterImgEntry.grid(row = 3, column = 0)
        try:
            monsterAvatar = ImageTk.PhotoImage(Image.open(f"img/{monsterToEdit[2]}").resize((150,150)))
            self.imageLabel = tk.Label(self.editMonsterFormFrame, image=monsterAvatar)
            self.imageLabel.image = monsterAvatar
            self.imageLabel.grid(row = 4, column = 0, pady = 5)
        finally:
            #create frame to hold buttons
            self.BtnFrame = tk.Frame(self.editMonsterFormFrame)
            self.BtnFrame.grid(row = 5, column = 0)
            self.BtnFrame.columnconfigure(0, weight=1) 
            self.BtnFrame.columnconfigure(1, weight=1) 
            self.BtnFrame.columnconfigure(2, weight=1)
            #button to submit updates
            self.editMonsterBtn = tk.Button(self.BtnFrame, text = "Update Monster", font = ("Times New Roman", 14), command = lambda: self.EditMonster(monster_id, self.editMonsterNameEntry.get(),self.editMonsterImgEntry.get(),self.editMonsterFormFrame )) 
            self.editMonsterBtn.grid(row = 0, column = 0, pady = 5, padx = 10)
            #button to cancel
            self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllMonsters(self.editMonsterFormFrame)) 
            self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 
        
    def EditMonster(self, id, name, img, frame):
        try:
            #add the monster with given info
            wanderingMonster.updateMonster(id, name, img)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Monster updated: {name}")
        except Exception as e:
            #alert user to error message and incomplete addition of monster.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Monster not updated.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
       
    def DeleteMonsterForm(self, monster_id, frame):
        #fetch monster
        monsterToDelete = wanderingMonster.getMonster(monster_id)
        print(f"Monster fetched: {monsterToDelete}")
        #convert monster info to TKString for default values
        monsterName = monsterToDelete[1]
        monsterImg = monsterToDelete[2]

        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.deleteMonsterFormFrame = tk.Frame(self)
        self.deleteMonsterFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.deleteMonsterFormFrame.columnconfigure(0, weight=1)
        self.deleteMonsterFormFrame.rowconfigure(0, weight=1)   
        #display confirmation msg
        self.deleteMonsterCfrmLabel = tk.Label(self.deleteMonsterFormFrame, text = "Are you sure you want to delete this monster?", font= ("Times New Roman", 18), wraplength=350, pady = 15, fg = "red")
        self.deleteMonsterCfrmLabel.grid(row = 0, column = 0)
        #display monster info
        self.deleteMonsterNameLabel = tk.Label(self.deleteMonsterFormFrame, text = f"Monster Name: {monsterName}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteMonsterNameLabel.grid(row = 1, column = 0)

        self.deleteMonsterImgLabel = tk.Label(self.deleteMonsterFormFrame, text = f"Monster Image: {monsterImg}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteMonsterImgLabel.grid(row = 2, column = 0)
        
        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.deleteMonsterFormFrame)
        self.BtnFrame.grid(row = 3, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)
        #button to confirm deletion
        self.deleteMonsterBtn = tk.Button(self.BtnFrame, text = "Delete Monster", font = ("Times New Roman", 14), command = lambda: self.DeleteMonster(monster_id,self.deleteMonsterFormFrame )) 
        self.deleteMonsterBtn.grid(row = 0, column = 0, pady = 5, padx = 10)
        #button to cancel
        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllMonsters(self.deleteMonsterFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 

    def DeleteMonster(self, monster_id, frame):
        print(f"DeleteMonster() reached. monster_id: {monster_id}" )
        try:
            #add the monster with given info
            wanderingMonster.deleteMonster(monster_id)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Monster deleted")
        except Exception as e:
            #alert user to error message and incomplete addition of monster.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Monster not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ACCESS QUESTIONS  # # # # # # # # # # # # # # # # # # # # # #
    def AccessQuestions(self, frame):
        self.destroyThing(frame)

        self.questionFrame = tk.Frame(self)
        self.questionFrame.grid(row = 0, column = 0)

        #welcome question 
        self.questionAccessLabel = tk.Label(self.questionFrame, text = "What would like to do?", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.questionAccessLabel.grid(row = 0, column = 0, pady = 5)
 
        #Option Buttons
        self.viewQuestionsBtn = tk.Button(self.questionFrame, text = "View All Questions", font = ("Times New Roman", 14), command = lambda: self.ViewAllQuestions(self.questionFrame)) 
        self.viewQuestionsBtn.grid(row = 1, column = 0, pady = 10)

        self.addQuestionBtn = tk.Button(self.questionFrame, text = "Add a Question", font = ("Times New Roman", 14), command = self.AddQuestionForm) 
        self.addQuestionBtn.grid(row = 2, column = 0, pady = 10)

        #home button
        self.homeBtn = tk.Button(self.questionFrame, text = "Home", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(frame=self.questionFrame)) 
        self.homeBtn.grid(row = 3, column = 0, pady = 5)  


    def ViewAllQuestions(self, frame):
        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.viewAllQuestionsFrame = ctk.CTkScrollableFrame(self, fg_color= "gray95")
        self.viewAllQuestionsFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.viewAllQuestionsFrame.columnconfigure(0, weight=1)
        self.viewAllQuestionsFrame.columnconfigure(1, weight=3)
        self.viewAllQuestionsFrame.columnconfigure(2, weight=3)
        self.viewAllQuestionsFrame.columnconfigure(3, weight=2)
        self.viewAllQuestionsFrame.columnconfigure(4, weight=2)
        self.viewAllQuestionsFrame.rowconfigure(0, weight=1)

        #hold headers to send for display
        headers = ["ID", "Question", "Answer", "Bank"]
        #hold questions in list to send for display
        questions.getAllQuestions()
        getQuestions = questions.allQuestions
        #send list for display
        self.displayList(getQuestions, headers, self.viewAllQuestionsFrame, "questions")     
        #home button
        self.homeBtn = tk.Button(self.viewAllQuestionsFrame, text = "Home", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(frame=self.viewAllQuestionsFrame)) 
        self.homeBtn.grid(row = 0, column = 4, pady = 5)           
    
    def AddQuestionForm(self):
        #Destroy the previous frame
        self.destroyThing(self.questionFrame)
        #New frame for this page
        self.addQuestionFormFrame = tk.Frame(self)
        self.addQuestionFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.addQuestionFormFrame.columnconfigure(0, weight=1)
        self.addQuestionFormFrame.rowconfigure(0, weight=1)   
        #create elements to collect data
        self.addQuestionLabel = tk.Label(self.addQuestionFormFrame, text = "Question", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addQuestionLabel.grid(row = 0, column = 0)

        self.addQuestionEntry = tk.Text(self.addQuestionFormFrame, height = 3, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addQuestionEntry.grid(row = 1, column = 0)

        self.addAnswerLabel = tk.Label(self.addQuestionFormFrame, text = "Answer", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addAnswerLabel.grid(row = 2, column = 0)

        self.addAnswerEntry = tk.Text(self.addQuestionFormFrame, height = 3, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addAnswerEntry.grid(row = 3, column = 0)

        self.addBankLabel = tk.Label(self.addQuestionFormFrame, text = "Bank", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.addBankLabel.grid(row = 4, column = 0)

        self.addBankEntry = tk.Entry(self.addQuestionFormFrame, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.addBankEntry.grid(row = 5, column = 0)

        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.addQuestionFormFrame)
        self.BtnFrame.grid(row = 6, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)
        #button to submit
        self.addQuestionBtn = tk.Button(self.BtnFrame, text = "Add Question", font = ("Times New Roman", 14), command = lambda: self.AddQuestion(self.addQuestionEntry.get("1.0", "end-1c"),self.addAnswerEntry.get("1.0", "end-1c"), self.addBankEntry.get(), self.addQuestionFormFrame )) 
        self.addQuestionBtn.grid(row = 0, column = 0, pady = 5, padx = 10)
        #button to cancel
        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllQuestions(self.addQuestionFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 

    def AddQuestion(self, question, answer, bank, frame):
        try:
            #add the question with given info
            questions.addQuestion(question, answer, bank)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Question added.")
        except Exception as e:
            #alert user to error message and incomplete addition of question.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Question not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
        

    def EditQuestionForm(self, question_id, frame):
        #fetch question
        questionToEdit = questions.getQuestion(question_id)
        #convert question info to TKString for default values
        questionText = questionToEdit[1]
        answerText = questionToEdit[2]
        bankText = tk.StringVar(value = questionToEdit[3])
        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.editQuestionFormFrame = tk.Frame(self)
        self.editQuestionFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.editQuestionFormFrame.columnconfigure(0, weight=1)
        self.editQuestionFormFrame.rowconfigure(0, weight=1)   
                
        #create elements to collect data
        self.editQuestionLabel = tk.Label(self.editQuestionFormFrame, text = "Question", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editQuestionLabel.grid(row = 0, column = 0)

        self.editQuestionEntry = tk.Text(self.editQuestionFormFrame, height = 3, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editQuestionEntry.grid(row = 1, column = 0)
        self.editQuestionEntry.insert("1.0", questionText )

        self.editAnswerLabel = tk.Label(self.editQuestionFormFrame, text = "Answer", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editAnswerLabel.grid(row = 2, column = 0)

        self.editAnswerEntry = tk.Text(self.editQuestionFormFrame, height = 3, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editAnswerEntry.grid(row = 3, column = 0)
        self.editAnswerEntry.insert("1.0", answerText )

        self.editBankLabel = tk.Label(self.editQuestionFormFrame, text = "Bank", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.editBankLabel.grid(row = 4, column = 0)

        self.editBankEntry = tk.Entry(self.editQuestionFormFrame, textvariable= bankText, font = ("Times New Roman", 14), bd = 5, relief="flat", borderwidth=10)
        self.editBankEntry.grid(row = 5, column = 0)

        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.editQuestionFormFrame)
        self.BtnFrame.grid(row = 6, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)
        #button to submit updates
        self.editQuestionBtn = tk.Button(self.BtnFrame, text = "Update Question", font = ("Times New Roman", 14), command = lambda: self.EditQuestion(question_id, self.editQuestionEntry.get("1.0", "end-1c"),self.editAnswerEntry.get("1.0", "end-1c"), self.editBankEntry.get(), self.editQuestionFormFrame )) 
        self.editQuestionBtn.grid(row = 0, column = 0, pady = 5, padx = 10)
        #button to cancel
        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllQuestions(self.editQuestionFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 

    def EditQuestion(self, id, question, answer, bank, frame):
        try:
            #add the question with given info
            questions.updateQuestion(id, question, answer, bank)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Question updated")
        except Exception as e:
            #alert user to error message and incomplete addition of question.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Question not updated.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
       
    def DeleteQuestionForm(self, question_id, frame):
        #fetch question
        questionToDelete = questions.getQuestion(question_id)
        print(f"Question fetched: {questionToDelete}")
        #convert question info to TKString for default values
        questionText = questionToDelete[1]
        answerText = questionToDelete[2]
        bankText = questionToDelete[3]

        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.deleteQuestionFormFrame = tk.Frame(self)
        self.deleteQuestionFormFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.deleteQuestionFormFrame.columnconfigure(0, weight=1)
        self.deleteQuestionFormFrame.rowconfigure(0, weight=1)   
        #display confirmation msg
        self.deleteQuestionCfrmLabel = tk.Label(self.deleteQuestionFormFrame, text = "Are you sure you want to delete this question?", font= ("Times New Roman", 18), wraplength=350, pady = 15, fg = "red")
        self.deleteQuestionCfrmLabel.grid(row = 0, column = 0)
        #display question info
        self.deleteQuestionLabel = tk.Label(self.deleteQuestionFormFrame, text = f"Question: {questionText}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteQuestionLabel.grid(row = 1, column = 0)

        self.deleteAnswerLabel = tk.Label(self.deleteQuestionFormFrame, text = f"Answer: {answerText}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteAnswerLabel.grid(row = 2, column = 0)

        self.deleteBankLabel = tk.Label(self.deleteQuestionFormFrame, text = f"Bank: {bankText}", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.deleteBankLabel.grid(row = 3, column = 0)
        #create frame to hold buttons
        self.BtnFrame = tk.Frame(self.deleteQuestionFormFrame)
        self.BtnFrame.grid(row = 4, column = 0)
        self.BtnFrame.columnconfigure(0, weight=1) 
        self.BtnFrame.columnconfigure(1, weight=1) 
        self.BtnFrame.columnconfigure(2, weight=1)
        #button to confirm deletion
        self.deleteQuestionBtn = tk.Button(self.BtnFrame, text = "Delete Question", font = ("Times New Roman", 14), command = lambda: self.DeleteQuestion(question_id,self.deleteQuestionFormFrame )) 
        self.deleteQuestionBtn.grid(row = 0, column = 0, pady = 5, padx = 10)
        #button to cancel
        self.cancelBtn = tk.Button(self.BtnFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllQuestions(self.deleteQuestionFormFrame)) 
        self.cancelBtn.grid(row = 0, column = 1, pady = 5, padx = 10) 

    def DeleteQuestion(self, question_id, frame):
        print(f"DeleteQuestion() reached. question_id: {question_id}" )
        try:
            #add the question with given info
            questions.deleteQuestion(question_id)
            #Destroy the previous frame
            self.destroyThing(frame)
            #send back to welcome screen
            self.WelcomeOptions(msg = f"Question deleted")
        except Exception as e:
            #alert user to error message and incomplete addition of question.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Question not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
    
# # # # # # # # # # #  BOSS BATTLE SET UP!  # # # # # # # # # #
 
    def BBSetup(self, frame):
        #Destroy the previous frame
        self.destroyThing(frame)
        #New frame for this page
        self.BBSetupFrame = tk.Frame(self)
        self.BBSetupFrame.grid(row = 0, column = 0, sticky = "news")
        #configure columns/rows
        self.BBSetupFrame.columnconfigure(0, weight=1)
        self.BBSetupFrame.rowconfigure(0, weight=1)   
                
        #create elements to collect data
        self.BBSetupLabel = tk.Label(self.BBSetupFrame, text = "Boss Battle \nComing Soon!", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.BBSetupLabel.grid(row = 0, column = 0)

        #button to cancel
        self.cancelBtn = tk.Button(self.BBSetupFrame, text = "Go Back", font = ("Times New Roman", 14), command = lambda: self.WelcomeOptions(self.BBSetupFrame)) 
        self.cancelBtn.grid(row = 1, column = 0, pady = 5, padx = 10) 

    def displayList(self, list, headers, frame, type):
        h = 0
        #create headers
        for header in headers:
            self.headerLabel = tk.Label(frame, text = header, font= ("Times New Roman", 18), wraplength=350, pady = 15)
            self.headerLabel.grid(row = 0, column = h, pady = 5)
            h += 1

        
        i = 0

        for item in list:
            id = item[0]
            j = 0
            for index in item:
                self.columnLabel = tk.Label(frame, text = index, font= ("Times New Roman", 14), wraplength=100, pady = 15)
                self.columnLabel.grid(row = i+1, column = j, pady = 5)
                j += 1
            
            match type:
                case "students":
                    self.editBtn = tk.Button(frame, text = "Edit", font = ("Times New Roman", 14), command = lambda id = id: self.EditStudentForm(id, frame)) 
                    self.editBtn.grid(row = i+1, column = len(headers), pady = 5)

                    self.deleteBtn = tk.Button(frame, text = "Delete", font = ("Times New Roman", 14), command = lambda id = id: self.DeleteStudentForm(id, frame)) 
                    self.deleteBtn.grid(row = i+1, column = len(headers)+1, pady = 5)
                case "monsters":
                    self.editBtn = tk.Button(frame, text = "Edit", font = ("Times New Roman", 14), command = lambda id = id: self.EditMonsterForm(id, frame)) 
                    self.editBtn.grid(row = i+1, column = len(headers), pady = 5)

                    self.deleteBtn = tk.Button(frame, text = "Delete", font = ("Times New Roman", 14), command = lambda id = id: self.DeleteMonsterForm(id, frame)) 
                    self.deleteBtn.grid(row = i+1, column = len(headers)+1, pady = 5)
                case "questions":
                    self.editBtn = tk.Button(frame, text = "Edit", font = ("Times New Roman", 14), command = lambda id = id: self.EditQuestionForm(id, frame)) 
                    self.editBtn.grid(row = i+1, column = len(headers), pady = 5, padx = 15)

                    self.deleteBtn = tk.Button(frame, text = "Delete", font = ("Times New Roman", 14), command = lambda id = id: self.DeleteQuestionForm(id, frame)) 
                    self.deleteBtn.grid(row = i+1, column = len(headers)+1, pady = 5, padx = 15)
            i += 1

    
    ##################### destroyThing() code used in previous project- not new code          
     #function to destroy things
    def destroyThing(self, thing):
        if thing: thing.destroy()   
    ##################### End of reused code





# # # # # # # # # # #  BOSS BATTLE SETUP  # # # # # # # # # #
#choose your arena!
#dropdown menu: Physics Unit 1, Physics Unit 2, Physics Unit 3

# # # # # # # # # # #  SETUP BATTLE  # # # # # # # # # #
#get question list
#get wandering monster
#get players
#display the  monster with name
#Start Battle

# # # # # # # # # # #  START BATTLE  # # # # # # # # # #
#if players is empty, reset players
#get current player
#Display monster, monster HP & player
#displayQuestion()

# # # # # # # # # # #  RUN GAME  # # # # # # # # # #

#display question
#display answer w/ correct/incorrect buttons

#ResultActions
#if correct, reduce monster HP

# # # # # # # # # # #  END GAME  # # # # # # # # # #
#if monsterHP == 0, you win
#elif Questions == 0, you lost
# else ask another question






if __name__ == "__main__":
    main()