from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)

# name,pet_type,level,start_date,start_time,duration, trainer, description
# make a function that calls in the CSV and make a dictionary of dictionaries
def get_courses():
    with open('courses.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile)
        courseInfo = {row['name']: {'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data}
    return courseInfo

# make the route for the index page
@app.route('/')
def index():
    courseInfo = get_courses()
    return render_template('index.html', courseInfo=courseInfo, )

# make a route for the course name and have the individual courses pop up when tapping on a course
@app.route('/courses/')
@app.route('/courses/<courseName>')
def courses(courseName=None):
    courseInfo = get_courses()
    if courseName in courseInfo.keys():
        course = courseInfo[courseName]
        return render_template('course.html', courseInfo=course, courseName=courseName)
    else:
        return render_template('courses.html', courseInfo=courseInfo)
