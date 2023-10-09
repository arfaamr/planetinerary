from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'  # Set the static folder to 'static'
app.static_url_path = '/static'  # Define the URL path for static files

@app.route('/')
def piapp():
    return render_template('piapp.html')
