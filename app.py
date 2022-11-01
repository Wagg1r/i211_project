from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
app = Flask(__name__)
  
# make a function that calls in the CSV and make a dictionary of dictionaries
COURSE_PATH = app.root_path + '/courses.csv'
COURSE_KEYS = ['name', 'pet_type', 'level', 'start_date', 'start_time', 'duration', 'trainer','description']

# this makes a list of dictionaries got from https://learnpython.com/blog/read-csv-into-list-python/
def get_courseList():
    with open(COURSE_PATH, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        courseList = [{'name': row['name'],'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data]
    return courseList

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
    courseList = get_courseList()
    return render_template('courses.html', courseList=courseList)

# !!!!!!!!!!!!!!!!!!!! this will need to be converted into a list !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/courses/<courseID>')
def course(courseID=None):
    courseList = get_courseList()
    courseID=int(courseID)
    course = courseList[courseID] #makes coursename
    return render_template('course.html', course=course)


@app.route('/courses/create', methods=['GET','POST'])
def create_course():
    course = get_courseList()
    if request.method == 'POST':
        course = get_courseList()
        new_dict = {}
        new_dict['name'] = request.form['courseName']
        new_dict['pet_type'] = request.form['pet_type']
        new_dict['level'] = request.form['level']
        new_dict['start_date'] = request.form['start_date']
        new_dict['start_time'] = request.form['start_time']
        new_dict['duration'] = request.form['duration']
        new_dict['trainer'] = request.form['trainer']
        new_dict['description'] = request.form['description']

        course.append(new_dict)
        set_course(course)
        return redirect(url_for('courses'))

    else:
        return render_template('course_form.html')

@app.route('/courses/<courseID>/edit', methods=['GET','POST'])
def edit(courseID=None):
    courseList = get_courseList()
    if request.method == 'POST':
        new_dict = {}
        new_dict['name'] = request.form['courseName']
        new_dict['pet_type'] = request.form['pet_type']
        new_dict['level'] = request.form['level']
        new_dict['start_date'] = request.form['start_date']
        new_dict['start_time'] = request.form['start_time']
        new_dict['duration'] = request.form['duration']
        new_dict['trainer'] = request.form['trainer']
        new_dict['description'] = request.form['description']

        courseList[int(courseID)] = new_dict
        set_course(courseList)
        return redirect(url_for('courses'))

    else:
        if courseID:
            courseList = get_courseList()
            courseID=int(courseID)
            course = courseList[courseID]
            return render_template('course_form.html',course=course, courseID=courseID)
        else:
            return render_template('course_form.html', courseID=courseID)


@app.route('/courses/<courseID>/delete')
def delete(courseID=None):
    courseList=get_courseList()
    if courseList:
        course = courseList[int(courseID)]
        delete=request.args.get('delete',None)
        if delete != None:
            courseList.pop(int(courseID))
            set_course(courseList)
        else:
            return render_template('delete_form.html',course=course, courseID=courseID)
    else:
        return redirect(url_for('courses'))
