import random
import sqlite3

class Monster():
    def __init__(self):
        self.HP = 12
    #list of all monsters in database
    allMonsters = []
    
    # return a random monster
    def randomMonster(self):
        shuffledList = random.shuffle(self.monsters)
        return shuffledList[0]
        
    #reduce monster HP by 1
    def reduceMonsterHP(self):
        if self.HP > 0:
            self.HP -= 1
    
    # return a random monster
    def randomMonster(self):
        randomPlayer = self.players[0]
        print("Before delete:" + randomPlayer)
        del self.players[0]
        print("After delete:" + randomPlayer)
        return randomPlayer
          
    #add monster
    def addMonster(self, name, img, bank):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #insert new monster
        addNewMonster = f"""INSERT INTO monsters (name, image, bank) 
        VALUES ('{name}', '{img}', '{bank}');"""
        c.execute(addNewMonster)
        #commit & close connection
        conn.commit()
        conn.close()
        print("Monster added")

    #get Monsters
    def getMonsters(self):
        #clear monster list
        self.allMonsters.clear()
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select all monsters
        c.execute("SELECT * FROM monsters")
        fetchedMonsters = c.fetchall()
        #add monsters to the list
        for monster in fetchedMonsters:
            self.allMonsters.append(monster)
        #commit & close connection
        conn.commit()
        conn.close()

    #get single monster by id
    def getMonster(self, monster_id):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #select monster
        c.execute(f"SELECT * FROM monsters WHERE monster_id = '{monster_id}'")
        fetchedMonster = c.fetchone()
        #commit & close connection
        conn.commit()
        conn.close()

        return fetchedMonster

    #modify monster
    def updateMonster(self, monster_id, name, img, bank):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #modify monster
        modifyMonster = f"""UPDATE monsters SET name = '{name}', image = '{img}', bank = '{bank}'
        WHERE monster_id = '{monster_id}';"""
        c.execute(modifyMonster)
        #commit & close connection
        conn.commit()
        conn.close()

   
    #delete monster
    def deleteMonster(self, monster_id):
        #connect & create cursor
        conn = self.openConnection()
        c = conn.cursor()
        #delete Monster
        removeMonster = f"""DELETE FROM monsters
        WHERE monster_id = '{monster_id}';"""
        c.execute(removeMonster)
        #commit & close connection
        conn.commit()
        conn.close()
    
    def openConnection(self):
        conn = sqlite3.connect('bossbattle.db')
        return conn
    