import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'        #! FIXME: actually gen secretkey lol

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

#change "added" attribute of activity in DB depending on checkboxes
@app.route('/mars_itinerary', methods =["GET", "POST"])
def setAdded():
    if request.method == "POST":
        addedList = []
        for i in range(1,4):                    #there are 3 activities for mars    ! TODO: get number of activities instead of hard-coding
            found = request.form.get(str(i))    #get input from checkboxes form
            if (found != None):
                addedList.append(i)

    conn = get_db_connection()
    cur = conn.cursor()

    for i in range(1,4):
        if i in addedList:
            cur.execute("UPDATE activities SET added=True WHERE id = ?", (i,))
        else:
            cur.execute("UPDATE activities SET added=False WHERE id = ?", (i,))         #if not selected, must reset value to false to wipe previous selections

    activities = cur.execute('SELECT * FROM activities').fetchall()
    conn.commit() 
    conn.close()   

    return render_template('itin.html', activities=activities)


#functions to redirect to next page
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
    return render_template('itin.html',activities=activities)               #! FIXME: setAdded() being used to direct to next page, not this (?). separate so this is used instead

@app.route('/lastPage')
def lastPage():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('lastPage.html',activities=activities)
