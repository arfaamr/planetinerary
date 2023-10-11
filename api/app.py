import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_activity(activity_id):
    conn = get_db_connection()
    activity = conn.execute('SELECT * FROM activities WHERE id = ?', (activity_id,)).fetchone()
    conn.close()
    if activity is None:
        abort(404)
    return activity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'        #! FIXME: actually gen secretkey lol

@app.route('/')
def index():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('index.html',activities=activities)

@app.route('/mars')
def mars():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('mars.html',activities=activities)

@app.route('/activity<int:activity_id>')
def activity(activity_id):
    conn = get_db_connection()
    conn.close()
    activity = get_activity(activity_id)
    return render_template('activity.html', activity=activity)

@app.route('/itinerary')
def itin():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('itin.html',activities=activities)

@app.route('/lastPage')
def lastPage():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('lastPage.html',activities=activities)


#set "added" attribute of activity to true after clicking checkbox
@app.route('/mars_itinerary', methods =["GET", "POST"])
def setAdded():
    if request.method == "POST":
        addedList = []
        for i in range(1,4):            #there r 3 activities for mars
            found = request.form.get(str(i))
            if (found != None):
                addedList.append(i)

    conn = get_db_connection()
    cur = conn.cursor()

    for i in range(1,4):            #there are 3 activities for mars
        if i in addedList:
            cur.execute("UPDATE activities SET added=True WHERE id = ?", (i,))
        else:
            cur.execute("UPDATE activities SET added=False WHERE id = ?", (i,))

    activities = cur.execute('SELECT * FROM activities').fetchall()

    conn.commit() 
    conn.close()   

    return render_template('itin.html', activities=activities)    #change this to next html page name ?