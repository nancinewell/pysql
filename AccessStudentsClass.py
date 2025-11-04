import tkinter as tk
import globals


class AccessStudents(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #configure rows/columns
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.AccessStudentsPortal(parent)

    def AccessStudentsPortal(self, frame):
        #Destroy the previous frame
        home.WhatToDo.destroyThing(frame)

        self.studentFrame = tk.Frame(self)
        self.studentFrame.grid(row = 0, column = 0)

        #welcome question 
        self.studentAccessLabel = tk.Label(self.studentFrame, text = "What would like to do?", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.studentAccessLabel.grid(row = 0, column = 0, pady = 5)
 
        #Option Buttons
        self.viewStudentsBtn = tk.Button(self.studentFrame, text = "View All Students", font = ("Times New Roman", 14), command = lambda: self.ViewAllStudents(self.studentFrame)) 
        self.viewStudentsBtn.grid(row = 1, column = 0, pady = 10)

        self.addStudentBtn = tk.Button(self.studentFrame, text = "Add a Student", font = ("Times New Roman", 14), command = lambda: self.AddStudentForm(self.studentFrame)) 
        self.addStudentBtn.grid(row = 2, column = 0, pady = 10)


    def ViewAllStudents(self, frame):
        #Destroy the previous frame
        home.WhatToDo.destroyThing(frame)
        #New frame for this page
        self.viewAllStudentsFrame = tk.Frame(self)
        self.viewAllStudentsFrame.grid(row = 0, column = 0)
        #configure columns/rows
        self.viewAllStudentsFrame.columnconfigure(0, weight=1)
        self.viewAllStudentsFrame.columnconfigure(1, weight=3)
        self.viewAllStudentsFrame.columnconfigure(2, weight=3)
        self.viewAllStudentsFrame.columnconfigure(3, weight=2)
        self.viewAllStudentsFrame.columnconfigure(4, weight=2)
        self.viewAllStudentsFrame.rowconfigure(0, weight=1)

        self.studentHeaderIdLabel = tk.Label(self.viewAllStudentsFrame, text = "ID", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.studentHeaderIdLabel.grid(row = 0, column = 0, pady = 5)

        self.studentHeaderNameLabel = tk.Label(self.viewAllStudentsFrame, text = "Name", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.studentHeaderNameLabel.grid(row = 0, column = 1, pady = 5)

        self.studentHeaderImgLabel = tk.Label(self.viewAllStudentsFrame, text = "Image", font= ("Times New Roman", 18), wraplength=350, pady = 15)
        self.studentHeaderImgLabel.grid(row = 0, column = 2, pady = 5)

        #ensure all newly added students are in the list
        globals.students.getStudents()
        getStudents = globals.students.allStudents
        i = 0

        for student in getStudents:
            studentId = student[0]

            self.studentIdLabel = tk.Label(self.viewAllStudentsFrame, text = student[0], font= ("Times New Roman", 14), wraplength=350, pady = 15)
            self.studentIdLabel.grid(row = i+1, column = 0, pady = 5)

            self.studentNameLabel = tk.Label(self.viewAllStudentsFrame, text = student[1], font= ("Times New Roman", 14), wraplength=350, pady = 15)
            self.studentNameLabel.grid(row = i+1, column = 1, pady = 5)

            self.studentImgLabel = tk.Label(self.viewAllStudentsFrame, text = student[2], font= ("Times New Roman", 14), wraplength=350, pady = 15)
            self.studentImgLabel.grid(row = i+1, column = 2, pady = 5)

            self.editStudentsBtn = tk.Button(self.viewAllStudentsFrame, text = "Edit", font = ("Times New Roman", 14), command = lambda studentId = studentId: self.EditStudentForm(studentId, self.viewAllStudentsFrame)) 
            self.editStudentsBtn.grid(row = i+1, column = 3, pady = 5)

            self.deleteStudentsBtn = tk.Button(self.viewAllStudentsFrame, text = "Delete", font = ("Times New Roman", 14), command = lambda studentId = studentId: self.DeleteStudentForm(studentId, self.viewAllStudentsFrame)) 
            self.deleteStudentsBtn.grid(row = i+1, column = 4, pady = 5)

            i += 1

            
    
    def AddStudentForm(self, frame):
        #Destroy the previous frame
        home.WhatToDo.destroyThing(frame)
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

        self.addStudentBtn = tk.Button(self.addStudentFormFrame, text = "Add Student", font = ("Times New Roman", 14), command = lambda: self.AddStudent(self.addStudentNameEntry.get(),self.addStudentImgEntry.get(),self.addStudentFormFrame )) 
        self.addStudentBtn.grid(row = 4, column = 0, pady = 5)

    def AddStudent(self, name, img, frame):
        try:
            #add the student with given info
            globals.students.addStudent(name, img)
            #Destroy the previous frame
            home.WhatToDo.destroyThing(frame)
            #send back to welcome screen
            home.WhatToDo.WelcomeOptions(msg = f"Student added: {name}")
        except Exception as e:
            #alert user to error message and incomplete addition of student.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Student not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
        

    def EditStudentForm(self, student_id, frame):
        #fetch student
        studentToEdit = globals.students.getStudent(student_id)
        #convert student info to TKString for default values
        studentName = tk.StringVar(value = studentToEdit[1])
        studentImg = tk.StringVar(value = studentToEdit[2])

        #Destroy the previous frame
        home.WhatToDo.destroyThing(frame)
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
        #button to submit updates
        self.editStudentBtn = tk.Button(self.editStudentFormFrame, text = "Update Student", font = ("Times New Roman", 14), command = lambda: self.EditStudent(student_id, self.editStudentNameEntry.get(),self.editStudentImgEntry.get(),self.editStudentFormFrame )) 
        self.editStudentBtn.grid(row = 4, column = 0, pady = 5)
        

    def EditStudent(self, id, name, img, frame):
        try:
            #add the student with given info
            globals.students.updateStudent(id, name, img)
            #Destroy the previous frame
            home.WhatToDo.destroyThing(frame)
            #send back to welcome screen
            home.WhatToDo.WelcomeOptions(msg = f"Student updated: {name}")
        except Exception as e:
            #alert user to error message and incomplete addition of student.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Student not updated.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)
       
    def DeleteStudentForm(self, student_id, frame):
        #fetch student
        studentToDelete = globals.students.getStudent(student_id)
        print(f"Student fetched: {studentToDelete}")
        #convert student info to TKString for default values
        studentName = studentToDelete[1]
        studentImg = studentToDelete[2]

        #Destroy the previous frame
        home.WhatToDo.destroyThing(frame)
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
        #button to confirm deletion
        self.deleteStudentBtn = tk.Button(self.deleteStudentFormFrame, text = "Delete Student", font = ("Times New Roman", 14), command = lambda: self.DeleteStudent(student_id,self.deleteStudentFormFrame )) 
        self.deleteStudentBtn.grid(row = 3, column = 0, pady = 5)
        #button to cancel
        self.cancelBtn = tk.Button(self.deleteStudentFormFrame, text = "Cancel", font = ("Times New Roman", 14), command = lambda: self.ViewAllStudents(self.deleteStudentFormFrame)) 
        self.cancelBtn.grid(row = 4, column = 0, pady = 5) 

    def DeleteStudent(self, student_id, frame):
        print(f"DeleteStudent() reached. student_id: {student_id}" )
        try:
            #add the student with given info
            globals.students.deleteStudent(student_id)
            #Destroy the previous frame
            home.WhatToDo.destroyThing(frame)
            #send back to welcome screen
            home.WhatToDo.WelcomeOptions(msg = f"Student deleted")
        except Exception as e:
            #alert user to error message and incomplete addition of student.
            self.errorMsg = tk.Label(frame, text = f"Error: {e}. Student not added.", font= ("Times New Roman", 12), wraplength=350, pady = 15, fg = "red")
            self.errorMsg.grid(row = 5, column = 0)