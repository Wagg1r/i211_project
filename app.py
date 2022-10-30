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



        # reading into a dictionaries of dictionaries
# def get_courseList():
#     try:
#         with open(COURSE_PATH, 'r') as csvfile:
#             data = csv.DictReader(csvfile)
#             CourseDict = {}
#             for course in data:
#                 CourseDict[course['id']] = course
#     except Exception as e:
#         print(e)
#     print(CourseDict)

       
# make a function that calls in the CSV and make a dictionary of dictionaries
COURSE_PATH = app.root_path + '/courses.csv'
COURSE_KEYS = ['id', 'name', 'pet_type', 'level', 'start_date', 'start_time', 'duration', 'trainer','description']

# this makes a list of dictionaries got from https://learnpython.com/blog/read-csv-into-list-python/
def get_courseList():
    with open(COURSE_PATH, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        courseList = list({'id': row['id'],'name': row['name'],'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data)
    # print(courseList)
    return courseList
    

# this makes a dictionary of dictionaries
# def get_courses():
#     with open(COURSE_PATH, 'r') as csvfile:
#         data = csv.DictReader(csvfile)
#         courseInfo = {row['id']: {'name': row['name'],'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data}
#     return courseInfo



# make the route for the index page
@app.route('/')
def index():
    courseList = get_courseList()
    return render_template('index.html', courseList=courseList)

# make a route for the course name and have the individual courses pop up when tapping on a course
@app.route('/courses/')
def courses():
    courseList = get_courseList()
    return render_template('courses.html', courseList=courseList)

# !!!!!!!!!!!!!!!!!!!! this will need to be converted into a list !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route('/courses/<courseName>')
def course(courseName=None):
    courseList = get_courseList()

    courseName=int(courseName)
    course = courseList[courseName] #makes coursename
    strID = str(courseName)
    return render_template('course.html', course=course, courseName=courseName, courseList=courseList)


# this takes the completed dictionary from the user and adds it to the cvs file i think this is where the error is because it is not appending to the list
def set_course(CourseInfo):
    try:
        with open(COURSE_PATH, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=COURSE_KEYS)
            writer.writeheader()
            for course in CourseInfo.values():
                course['id'].append(writer.writerow(course))
    except Exception as err:
        print(err)




@app.route('/create', methods=['GET','POST'])
def create_course():
    course = get_courseList()
    if request.method == 'POST':
        course = get_courseList()
        new_dict = {}
        new_dict['id'] = request.form['id']
        new_dict['name'] = request.form['courseName']
        new_dict['pet_type'] = request.form['pet_type']
        new_dict['level'] = request.form['level']
        new_dict['start_date'] = request.form['start_date']
        new_dict['start_time'] = request.form['start_time']
        new_dict['duration'] = request.form['duration']
        new_dict['trainer'] = request.form['trainer']
        new_dict['description'] = request.form['description']
# !!!!!!!!!!!!!!!!!!!!!!!!!!! this is messing up because i am not getting into the nested dictionary it is over riding the top layer of dictionary, i want to be in the nested dictionary
        course [len(course)+1] = new_dict
        set_course(course)
        return redirect(url_for('courses'))

    else:
        courseList=get_courseList()
        return render_template('course_form.html',courseList=courseList)
