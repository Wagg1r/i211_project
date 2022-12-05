import pymysql
#uncomment the following line when you start project 3.2:
from app import app
# Make sure you have data in your tables. You should have used auto increment for 
# primary keys, so all primary keys should start with 1
#you will need this helper function for all of your functions
#Use the uncommented version to test and turn in your code.  
#Comment out this version and then uncomment and use the second version below when you are importing 
#this file into your app.py in your I211_project for Project 3.2
# def get_connection():
#     return pymysql.connect(host="db.luddy.indiana.edu",
#                            user="i211f22_thomwagg",
#                            password="my+sql=i211f22_thomwagg",
#                            database="i211f22_thomwagg",
#                            cursorclass=pymysql.cursors.DictCursor)
def get_connection():
    return pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           password=app.config['DB_PASS'],
                           database=app.config['DB_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor)
def get_courses():
    #Returns a list of dictionaries representing all of the courses data
    #add your code below, deleting the "pass"
    sql = "SELECT * FROM courses"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

def get_course(course_id):
    #Takes a course_id, returns a single dictionary containing the data for a course with that id
    sql = "SELECT * FROM courses WHERE course_id =%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,course_id)
            return cursor.fetchall()
            #return course here? something like "course =cursor.fetchall()"

def add_course(course):
    #Takes as input all of the data for a course. Inserts a new course into the course table
    sql = "INSERT INTO courses (name,pet_type,level, start_date, start_time, duration, length, trainer, description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (course["name"],course["pet_type"],course["level"],course["start_date"], course["start_time"], course["duration"], course["length"], course["trainer"], course["description"]))
        conn.commit()

def update_course(course_id, course):
    #Takes a course_id and data for a course. Updates the course table with new data for the course with
    #course_id as it's primary key
    sql = "UPDATE courses SET name=%s,pet_type=%s,level=%s, start_date=%s, start_time=%s, duration=%s, length=%s, trainer=%s, description=%s WHERE course_id =%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (course["name"],course["pet_type"],course["level"],course["start_date"], course["start_time"], course["duration"], course["length"], course["trainer"], course["description"], course_id))
        conn.commit()


def delete_course(course_id):
    #Takes an attendee_id and deletes the attendee with that attendee_id from the attendee table
    sql = "DELETE FROM courses WHERE course_id =%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,course_id)
        conn.commit()

def get_attendees(course_id):
    #Takes a course_id and returns a list of the dictionaries of all attendees for that course
    sql = "select * from attendee where course_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (course_id))
            return cursor.fetchall()

def get_attendee(attendee_id):
    #Takes a course_id and returns a list of the dictionaries of all attendees for that course
    sql = "select * from attendee where attendee_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (attendee_id))
            return cursor.fetchall()


def add_attendee(course_id, attendee):
    #Given a course_id and attendee info, adds a new attendee to the attendee table
    sql = "INSERT INTO attendee (course_id,f_name, l_name, phone_num, email, dob) VALUES (%s,%s,%s,%s,%s,%s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(course_id,attendee["f_name"], attendee["l_name"], attendee["phone_num"], attendee["email"], attendee["dob"]))
        conn.commit()

def edit_attendee(f_name, l_name, phone_num, email, dob, attendee_id): 
    #Given an attendee__id and attendee info, updates the data for the attendee with the given attendee_id the attendee table
    sql = "UPDATE attendee SET f_name=%s, l_name=%s, phone_num=%s, email=%s, dob=%s WHERE attendee_id =%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (f_name, l_name, phone_num, email, dob, attendee_id))
        conn.commit()


def delete_attendee(attendee_id):
    #Takes an attendee_id and deletes the attendee with that attendee_id from the attendee table
    sql = "DELETE FROM attendee WHERE attendee_id =%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,attendee_id)
        conn.commit()

def delete_attendees(course_id):
    #Takes an attendee_id and deletes the attendee with that attendee_id from the attendee table
    sql = "DELETE FROM attendee WHERE course_id =%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,course_id)
        conn.commit()

if __name__ == '__main__':
    #add more test code here to make sure your functions are working correctly
    try:
        # print(f'All courses: {get_courses()}')
        # print(f'Course info for course_id 1: {get_course(1)}')
        course_dic={"name":"thomas", "pet_type":"dog", "level":"beginner", "start_date":"2022-12-03", "start_time":"09:00:00", "duration":60, "length":6, "trainer":"Lassie Shepherd", "description":"For newbie dog owners!"}
        
        # add_course(course_dic)
        # update_course(11,course_dic)
        add_attendee_dic={"course_id":4,"f_name":"Axle","l_name":"connor", "phone_num":"(888)-888-8888","email":"con@gmail.com","dob":"1946-07-01"}
        edit_attendee_dic={"course_id":3,"f_name":"barry","l_name":"connor", "phone_num":"(888)-888-8888","email":"con@gmail.com","dob":"1946-07-01"}
        # add_attendee(1,attendee_dic)
        edit_attendee(6,edit_attendee_dic)
        delete_attendee(6)
    except Exception as e:
        print(e)
