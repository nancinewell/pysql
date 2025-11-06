import random
import sqlite3

class Question():
    def __init__(self):
        pass

    #list of all questions in the selected bank
    allQuestions = []
    questionsFromBank = []
    randomQuestion = None
    # return a random question
    def randomQuestionSelection(self):
        #grab the first shuffled question
        self.randomQuestion = self.questionsFromBank[0]
        #remove question from list
        del self.questionsFromBank[0]
        #return question
        return self.randomQuestion
           
    #add question
    def addQuestion(self, question, answer, bank):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #insert new question
        addNewQuestion = f"""INSERT INTO questions (question, answer, bank) 
        VALUES('{question}', '{answer}', '{bank}')"""
        c.execute(addNewQuestion)
        #commit & close connection
        conn.commit()
        conn.close()

    #get all questions
    def getAllQuestions(self):
    #clear allQuestions list
        self.allQuestions.clear()
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select all questions
        c.execute(f"SELECT * FROM questions")
        selectedQuestions = c.fetchall()
        #add questions to the list
        for question in selectedQuestions:
            self.allQuestions.append(question)
        #commit & close connection
        conn.commit()
        conn.close()

    def getAllQuestionsWithMonster(self):
    #clear allQuestions list
        self.allQuestions.clear()
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select all questions
        #use inner join to gather questions and monsters that go to this fight
        getQandM = f"""SELECT question_id, question, answer, name, questions.bank
        FROM questions
        INNER JOIN monsters on monsters.bank = questions.bank
        """
        c.execute(getQandM)
        selectedQuestions = c.fetchall()
        #add questions to the list
        for question in selectedQuestions:
            self.allQuestions.append(question)
        #commit & close connection
        conn.commit()
        conn.close()
        
    
    #get questions from bank
    def getQuestions(self, bank):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select all questions
        c.execute(f"SELECT * FROM questions WHERE bank = '{bank}'")
        selectedQuestions = c.fetchall()
        #add questions to the list
        for question in selectedQuestions:
            self.questionsFromBank.append(question)
        #commit & close connection
        conn.commit()
        conn.close()
        #shuffle questions
        self.questions = random.shuffle(self.questionsFromBank)

    #get single question by id
    def getQuestion(self, question_id):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select question
        c.execute(f"SELECT * FROM questions WHERE question_id = '{question_id}'")
        fetchedQuestion = c.fetchone()
        #commit & close connection
        conn.commit()
        conn.close()

        return fetchedQuestion

    #modify question
    def updateQuestion(self, question_id, question, answer, bank):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #modify question
        modifyQuestion = f"""UPDATE questions SET question = '{question}', answer = '{answer}', bank = '{bank}'
        WHERE question_id = '{question_id}'
        """
        c.execute(modifyQuestion)
        #commit & close connection
        conn.commit()
        conn.close()
   
    #delete question
    def deleteQuestion(self, question_id):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #delete question
        removeQuestion = f"""DELETE from questions
        WHERE question_id = '{question_id}'
        """
        c.execute(removeQuestion)
        #commit & close connection
        conn.commit()
        conn.close()
    
    #get list of unique banks
    def getBanks(self):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select all questions
        c.execute(f"SELECT DISTINCT bank FROM questions")
        banks = c.fetchall()
        bank = []
        #add questions to the list
        for item in banks:
            bank.append(str(item[0]))
        #commit & close connection
        conn.commit()
        conn.close()
        return bank


    def openConnection(self):
        conn = sqlite3.connect('bossbattle.db')
        return conn