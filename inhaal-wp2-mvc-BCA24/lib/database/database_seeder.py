import sqlite3

class DatabaseSeeder :
    def insert_events (self):
        events = [
            {"name": "Event 1", "description": "Description 1", "event_date": "2021-05-01", "start_time": "10:00", "end_time": "12:00", "location": "Location 1", "agenda_id": 1, "date_created": "2021-05-01"},	
            {"name": "Event 2", "description": "Description 2", "event_date": "2021-05-02", "start_time": "10:00", "end_time": "12:00", "location": "Location 2", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 3", "description": "Description 3", "event_date": "2021-05-03", "start_time": "10:00", "end_time": "12:00", "location": "Location 3", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 4", "description": "Description 4", "event_date": "2021-05-04", "start_time": "10:00", "end_time": "12:00", "location": "Location 4", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 5", "description": "Description 5", "event_date": "2021-05-05", "start_time": "10:00", "end_time": "12:00", "location": "Location 5", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 6", "description": "Description 6", "event_date": "2021-05-06", "start_time": "10:00", "end_time": "12:00", "location": "Location 6", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 7", "description": "Description 7", "event_date": "2021-05-07", "start_time": "10:00", "end_time": "12:00", "location": "Location 7", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 8", "description": "Description 8", "event_date": "2021-05-08", "start_time": "10:00", "end_time": "12:00", "location": "Location 8", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 9", "description": "Description 9", "event_date": "2021-05-09", "start_time": "10:00", "end_time": "12:00", "location": "Location 9", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 10", "description": "Description 10", "event_date": "2021-05-10", "start_time": "10:00", "end_time": "12:00", "location": "Location 10", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 11", "description": "Description 11", "event_date": "2021-05-01", "start_time": "10:00", "end_time": "12:00", "location": "Location 1", "agenda_id": 1, "date_created": "2021-05-01"},	
            {"name": "Event 12", "description": "Description 12", "event_date": "2021-05-02", "start_time": "10:00", "end_time": "12:00", "location": "Location 2", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 13", "description": "Description 13", "event_date": "2021-05-03", "start_time": "10:00", "end_time": "12:00", "location": "Location 3", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 14", "description": "Description 14", "event_date": "2021-05-04", "start_time": "10:00", "end_time": "12:00", "location": "Location 4", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 15", "description": "Description 15", "event_date": "2021-05-05", "start_time": "10:00", "end_time": "12:00", "location": "Location 5", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 16", "description": "Description 16", "event_date": "2021-05-06", "start_time": "10:00", "end_time": "12:00", "location": "Location 6", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 17", "description": "Description 17", "event_date": "2021-05-07", "start_time": "10:00", "end_time": "12:00", "location": "Location 7", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 18", "description": "Description 18", "event_date": "2021-05-08", "start_time": "10:00", "end_time": "12:00", "location": "Location 8", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 19", "description": "Description 19", "event_date": "2021-05-09", "start_time": "10:00", "end_time": "12:00", "location": "Location 9", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 20", "description": "Description 20", "event_date": "2021-05-10", "start_time": "10:00", "end_time": "12:00", "location": "Location 10", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 21", "description": "Description 21", "event_date": "2021-05-01", "start_time": "10:00", "end_time": "12:00", "location": "Location 1", "agenda_id": 1, "date_created": "2021-05-01"},	
            {"name": "Event 22", "description": "Description 22", "event_date": "2021-05-02", "start_time": "10:00", "end_time": "12:00", "location": "Location 2", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 23", "description": "Description 23", "event_date": "2021-05-03", "start_time": "10:00", "end_time": "12:00", "location": "Location 3", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 24", "description": "Description 24", "event_date": "2021-05-04", "start_time": "10:00", "end_time": "12:00", "location": "Location 4", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 25", "description": "Description 25", "event_date": "2021-05-05", "start_time": "10:00", "end_time": "12:00", "location": "Location 5", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 26", "description": "Description 26", "event_date": "2021-05-06", "start_time": "10:00", "end_time": "12:00", "location": "Location 6", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 27", "description": "Description 27", "event_date": "2021-05-07", "start_time": "10:00", "end_time": "12:00", "location": "Location 7", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 28", "description": "Description 28", "event_date": "2021-05-08", "start_time": "10:00", "end_time": "12:00", "location": "Location 8", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 29", "description": "Description 29", "event_date": "2021-05-09", "start_time": "10:00", "end_time": "12:00", "location": "Location 9", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 30", "description": "Description 30", "event_date": "2021-05-10", "start_time": "10:00", "end_time": "12:00", "location": "Location 10", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 31", "description": "Description 31", "event_date": "2021-05-01", "start_time": "10:00", "end_time": "12:00", "location": "Location 1", "agenda_id": 1, "date_created": "2021-05-01"},	
            {"name": "Event 32", "description": "Description 32", "event_date": "2021-05-02", "start_time": "10:00", "end_time": "12:00", "location": "Location 2", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 33", "description": "Description 33", "event_date": "2021-05-03", "start_time": "10:00", "end_time": "12:00", "location": "Location 3", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 34", "description": "Description 34", "event_date": "2021-05-04", "start_time": "10:00", "end_time": "12:00", "location": "Location 4", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 35", "description": "Description 35", "event_date": "2021-05-05", "start_time": "10:00", "end_time": "12:00", "location": "Location 5", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 36", "description": "Description 36", "event_date": "2021-05-06", "start_time": "10:00", "end_time": "12:00", "location": "Location 6", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 37", "description": "Description 37", "event_date": "2021-05-07", "start_time": "10:00", "end_time": "12:00", "location": "Location 7", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 38", "description": "Description 38", "event_date": "2021-05-08", "start_time": "10:00", "end_time": "12:00", "location": "Location 8", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 39", "description": "Description 39", "event_date": "2021-05-09", "start_time": "10:00", "end_time": "12:00", "location": "Location 9", "agenda_id": 1, "date_created": "2021-05-01"},
            {"name": "Event 40", "description": "Description 40", "event_date": "2021-05-10", "start_time": "10:00", "end_time": "12:00", "location": "Location 10", "agenda_id": 1, "date_created": "2021-05-01"},
            
        ]
        connection = sqlite3.connect('databases/event_calendar.db')
        cursor = connection.cursor()
        for event in events:
            cursor.execute("INSERT INTO events (name, description, event_date, start_time, end_time, location, agenda_id, date_created) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (event["name"], event["description"], event["event_date"], event["start_time"], event["end_time"], event["location"], event["agenda_id"], event["date_created"]))
        connection.commit()
        connection.close()
        print("✅ Demo data events created")

if __name__ == "__main__":
    note_model = DatabaseSeeder()
    note_model.insert_events()