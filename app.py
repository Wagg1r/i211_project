from flask import Flask, render_template, url_for
import csv
app = Flask(__name__)

# name,pet_type,level,start_date,start_time,duration

with open('courses.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)
    courseInfo = {row['name']: {'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration']} for row in data}

@app.route('/')
def index():
    return render_template('index.html', courseInfo=courseInfo, )

@app.route('/courses/')
def courses():
    return render_template('courses.html', courseInfo=courseInfo)