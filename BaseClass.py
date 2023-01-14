import sqlite3


class Create_cursor():


    def __init__(self,file_name):
    #Open Database
        self.file_name = file_name

        try:
            self.conn = sqlite3.connect(self.file_name)
        except Error as e:
            print(e)

        # Create a cursor to allow to execute SQL commands
        self.cursor = self.conn.cursor()

    def Create_Table(self):

        # Create a SQL Table
        sql_command = '''
                         CREATE TABLE IF NOT EXISTS contacts (
                             Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             Eng_word TEXT, 
                             Translation TEXT,
                             Progress INTEGER, 
                             Time INTEGER
                         )'''

        self.cursor.execute(sql_command)
        print('Base with words sucsfully open')

        # Commit the changes to the database
        self.conn.commit()

    def Create_Memory_Table(self):

        # Create a SQL Table
        sql_command = '''
                         CREATE TABLE IF NOT EXISTS contacts (
                             Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             Right_ans INTEGER,
                             RT INTEGER,
                             RB INTEGER,
                             LT INTEGER,
                             LB INTEGER, 
                             Ans INTEGER,
                             Positon NULL                           
                         )'''

        self.cursor.execute(sql_command)
        print('Log Base sucsfully open')

        # Commit the changes to the database
        self.conn.commit()

    def Print_Data(self):

        select_data = 'SELECT * FROM contacts'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)



    def Write_New_Word(self, word):
        # Create the sqlite database if it does not exist. If it exist, connect to it.

        insert_data = f"""
                INSERT INTO contacts 
                (Eng_word, Translation, Progress, Time) 
                VALUES ( 
                    '{word['Eng_word']}',
                    '{word['Translation']}',
                    '{word['Progress']}',
                    '{word['Time']}'
                )
            """
        self.cursor.execute(insert_data)
        # Commit the changes to the database
        self.conn.commit()
        print("Record new word successfully")

    def Write_Genereted_Answer(self, log):
        # Create the sqlite database if it does not exist. If it exist, connect to it.

        insert_data = f"""
                INSERT INTO contacts 
                (Right_ans,RT,RB,LT,LB,Ans,Positon) 
                VALUES ( 
                    '{log['Right_ans']}',
                    '{log['RT']}',
                    '{log['RB']}',
                    '{log['LT']}', 
                    '{log['LB']}',  
                    '{log['Ans']}',
                    '{log['Position']}'                 
                )
            """
        self.cursor.execute(insert_data)
        # Commit the changes to the database
        self.conn.commit()
        print("Record new word successfully")

    def Delete_Record(self,number):

            # Deleting single record now
            sql_update_query = """DELETE from contacts where id = ?"""
            self.cursor.execute(sql_update_query, (number,))
            self.conn.commit()
            print("Record deleted successfully ")


    def Number_Of_Elements(self):

        select_data = 'SELECT * FROM contacts'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()
        i = 0
        for row in rows:
            i = i + 1

        #print(i)
        return i

    def Pick_Up_Single_Value(self,num_field,column):

        select_data = 'SELECT * FROM contacts'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()
        row = rows[num_field]
        #print(row[column])
        return row[column]

    def Update_progress_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Progress = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        #print("Запись успешно обновлена")

    def Update_time_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Time = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        #print("Запись успешно обновлена")

    def Update_position_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Positon = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        #print("Запись успешно обновлена")

    def Update_ans_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Ans = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        #print("Запись успешно обновлена")

    def Update_word_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Eng_word = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        print("Запись успешно обновлена")

    def Update_translate_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Translation = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        print("Запись успешно обновлена")

    def Update_time_value(self,dev_id,num_field):
        sql_update_query = """Update contacts set Time = ? where id = ?"""
        data = (num_field,dev_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        print("Запись успешно обновлена")


    def Close_Database(self):
        self.conn.close()

