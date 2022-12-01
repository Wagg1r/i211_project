from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
app = Flask(__name__)
import database  
from os.path import exists
import html

# app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')
import database
# make a function that calls in the CSV and make a dictionary of dictionaries
COURSE_PATH = app.root_path + '/courses.csv'
COURSE_KEYS = ['name', 'pet_type', 'level', 'start_date', 'start_time', 'duration', 'length', 'trainer','description']

# this makes a list of dictionaries got from https://learnpython.com/blog/read-csv-into-list-python/
# def get_courseList():
#     with open(COURSE_PATH, 'r') as csvfile:
#         data = csv.DictReader(csvfile)
#         courseList = [{'name': row['name'],'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data]
#     return courseList



# this takes the completed dictionary from the user and adds it to the cvs file i think this is where the error is because it is not appending to the list
def set_course(courseList):
    try:
        with open(COURSE_PATH, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=COURSE_KEYS)
            writer.writeheader()
            for courses in courseList:
                writer.writerow(courses)
    except Exception as err:
        print(err)

# make the route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# make a route for the course name and have the individual courses pop up when tapping on a course
@app.route('/courses/')
def courses():
    courseList = database.get_courses()
    return render_template('courses.html', courseList=courseList)

# !!!!!!!!!!!!!!!!!!!! this will need to be converted into a list !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/courses/<course_id>')
def course(course_id=None):
    course_id=int(course_id)
    
    course =database.get_course(course_id) #makes coursename
    return render_template('course.html', course=course, course_id=course_id)

@app.route('/courses/create', methods=['GET','POST'])
def create_course():
    course = database.get_courses()
    course = {}
    if request.method == 'POST':
        course = database.get_courses()
        new_dict = {}
        new_dict['name'] = html.escape(request.form['name'])
        new_dict['pet_type'] = request.form['pet_type']
        new_dict['level'] = request.form['level']
        new_dict['start_date'] = request.form['start_date']
        new_dict['start_time'] = request.form['start_time']
        new_dict['duration'] = request.form['duration']
        new_dict['length'] = request.form['length']
        new_dict['trainer'] = html.escape(request.form['trainer'])
        new_dict['description'] = html.escape(request.form['description'])

        database.add_course(new_dict)
       # database.add_course(course)
        return redirect(url_for('courses'))

    else:
        return render_template('course_form.html', course = course)

@app.route('/courses/<course_id>/edit', methods=['GET','POST'])
def edit(course_id=None):
    courseList = database.get_courses()
    if request.method == 'POST':
        new_dict = {}
        new_dict['name'] = html.escape(request.form['name'])
        new_dict['pet_type'] = request.form['pet_type']
        new_dict['level'] = request.form['level']
        new_dict['start_date'] = request.form['start_date']
        new_dict['start_time'] = request.form['start_time']
        new_dict['duration'] = request.form['duration']
        new_dict['length'] = request.form['length']
        new_dict['trainer'] = html.escape(request.form['trainer'])
        new_dict['description'] = html.escape(request.form['description'])
########################### do i need -1?
        courseList[int(course_id)-1] = new_dict
        database.update_course(course_id, new_dict)
        return redirect(url_for('courses'))

    else:
        if course_id:
            courseList = database.get_courses()
            course_id=(int(course_id)-1)
            ####################################### i shouldn't have -1 probably?
            course = courseList[int(course_id)]
            return render_template('course_form.html',course=course, course_id=course_id)
        else:
            return render_template('course_form.html', course_id=course_id ,course=course)


@app.route('/courses/<course_id>/delete')
def delete(course_id=None):
    courseList=database.get_courses()
    if courseList:
        course = courseList[int(course_id)-1]
        delete=request.args.get('delete',None)
        if delete != None:
            courseList.pop(int(course_id)-1)
            database.delete_course(course_id)
            return redirect(url_for('courses'))

        else:
            return render_template('delete_form.html',course=course, course_id=course_id)
    else:
        return redirect(url_for('courses'))
