from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
app = Flask(__name__)

# this was my attempt at making a sorted list for date it didn't run properly so i have commented it out here
#         date = sorted(courseInfo, key = lambda item : datetime.strptime(item["start_date"],"%B %d %Y"))
        # dateList = list(csv.reader(COURSE_PATH, delimiter=","))
        # date = sorted(dateList, key = lambda item : datetime.strptime(item["start_date"],"%B %d %Y"))
        # year = {'January': 1, 'Febuary': 2, 'March': 3, 'April':4, 'May': 5, 'June': 6, 'July': 7 ,'August': 8 , 'September': 9, 'October': 10, 'November':11, 'December':12}
        # ind= 'October 19 2022'
        # res= ind.split(' ')
        # []

        
# make a function that calls in the CSV and make a dictionary of dictionaries
COURSE_PATH = app.root_path + '/courses.csv'
def get_courses():
    with open(COURSE_PATH, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        courseInfo = {row['name']: {'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data}
    return courseInfo
get_courses()
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




