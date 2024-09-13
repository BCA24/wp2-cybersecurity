from flask import Flask, render_template, request, redirect, url_for, flash, session
from lib.database.users_sql import NoteModel


app = Flask(__name__)
app.secret_key = "mysecretkey"

# def get_user_model():
#     if "user_model" not in session:
#         session["user_model"] = UserModel()
#     return session["user_model"]

@app.route("/welcome")
def welcome():
    return render_template('mainLogin.html')

@app.route("/agenda" )
def guestAgenda():
    note_model = NoteModel()
    page = request.args.get('page', 1, type=int)
    user_role = session.get('user_role')
    offset = (page-1)*20
    agendas = note_model.get_agenda('databases/event_calendar.db', agenda_name="agenda")

    return render_template('agenda.html.jinja', title = "Agenda", agendas = agendas, page = page, user_role=user_role)

@app.route("/agenda/<string:agenda_name>")
def agendaname(agenda_name):
    note_model = NoteModel()
    user_role = session.get('user_role')
    page = request.args.get('page', 1, type=int)
    all_events = note_model.get_event_by_name('databases/event_calendar.db', agenda_name)
    events_per_page = 20
    total_pages = (len(all_events) + events_per_page - 1) // events_per_page
    events = all_events[(page-1)*events_per_page:page*events_per_page]
    return render_template('agendaName.html.jinja', is_ingelogd=session.get("is_ingelogd", False), title = "Agenda", events = events, page = page, total_pages=total_pages, agenda_name=agenda_name, user_role = user_role)



@app.route("/agenda")
def agenda():
    return render_template("agenda.html", is_ingelogd=session.get("is_ingelogd", False))

@app.route("/user/<string:username>")
def userAgenda(username):
    return "User Agenda"

@app.route("/user/login", methods=["GET", "POST"])
def userLogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_model = NoteModel()
        user = user_model.get_user_by_users('databases/event_calendar.db', username, password)
        if user:
            session['user_role'] = 'user'
            session["user"] = user['username']
            session["is_ingelogd"] = True
            return redirect(url_for("agenda"))
        else:
            flash("Invalid username or password")
    return render_template("userLogin.html")

from flask import request
import sqlite3

@app.route("/create/agenda", methods=["GET", "POST"])
def createAgenda():
    if 'user' not in session:
        return redirect(url_for("welcome"))
    if  request.method == "POST":
        url_name = request.form.get("url_name")
        title = request.form.get("title")
        external_stylesheet = request.form.get("external_stylesheet")
        date_created = request.form.get("date_created")

        connection = sqlite3.connect('databases/event_calendar.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO agendas ( url_name, title, external_stylesheet, date_created) VALUES ( ?, ?, ?, ?)", ( url_name, title, external_stylesheet, date_created))
        connection.commit()
        connection.close()

    return render_template("newAgenda.html")

@app.route("/create/event", methods=["GET", "POST"])
def createEvent():
    if 'user' not in session:
        return redirect(url_for("welcome"))
    if request.method == "POST":
        name = request.form.get("naam")
        description = request.form.get("description")
        event_date = request.form.get("event_date")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")
        location = request.form.get("location")
        agenda_id = request.form.get("agenda_id")

        connection = sqlite3.connect('databases/event_calendar.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO events ( name, description, event_date, start_time, end_time, location, agenda_id) VALUES (?, ?, ?, ?, ?, ?, ?)", ( name, description, event_date, start_time, end_time, location, agenda_id))
        connection.commit()
        connection.close()

    return render_template("newEvent.html")

@app.route("/admin/login", methods=["GET", "POST"])
def adminLogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_model = NoteModel()
        user = user_model.get_user_by_admin('databases/event_calendar.db', username, password)
        if user:
            session['user_role'] = 'admin'
            session["user"] = user['username']  
            session["is_ingelogd"] = True
            return redirect(url_for("agenda"))
        else:
            flash("Invalid username or password")
    return render_template("adminLogin.html")

@app.route("/test")
def testRoute():
    if session.get("is_ingelogd") == True:
        return("Ik was al ingelogd en laat nu de pagina zien")
    else:
        return("ik ben nog niet ingelogd")


@app.route('/event/<string:events_name>')
def event(events_name):
    note_model = NoteModel()
    event = note_model.all_from_one_event('databases/event_calendar.db', events_name)

    return render_template('specificEvent.html', title = "Agenda", events = event)

@app.route("/logout", methods=["GET"])
def logout():
    if 'username'  in session:
        del session['username']
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(port=5001, debug=True)