import sqlite3
class NoteModel :
    def allnotes (self,db, event_name):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM events LIMIT 20 OFFSET ?", (event_name,))
        return cursor.fetchall()
    
    def get_agenda (self,db, agenda_name):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM agendas")
        return cursor.fetchall()


    # def __init__(self, db_path):
    #     self.conn = sqlite3.connect(db_path)
    #     self.cursor = self.conn.cursor()

    # def get_event_by_name(self, name):
    #     self.cursor.execute("SELECT * FROM events WHERE name = ?", (name,))
    #     event = self.cursor.fetchone()
    #     return event

    def get_event_by_name (self,db, agenda_name):
    
        connection = sqlite3.connect(db)
        print(agenda_name)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM events INNER JOIN agendas ON events.agenda_id = agendas.id WHERE agendas.url_name = ?", (agenda_name,))
        return cursor.fetchall()
    


    def get_user_by_admin(self, db, username, password):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ? AND is_admin = 1", (username, password))
        user = cursor.fetchone()
        return user

    def get_user_by_users(self, db, username, password):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ? AND is_admin = 0", (username, password))
        user = cursor.fetchone()
        return user
    
    def all_from_one_event (self,db, event_name):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM events WHERE name = ?", (event_name,))
        return cursor.fetchall()
