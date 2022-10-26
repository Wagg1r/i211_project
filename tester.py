from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
app = Flask(__name__)

with open('courses.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)
    courseInfo = {row['name']: {'pet_type': row['pet_type'], 'level': row['level'], 'start_date': row['start_date'], 'start_time': row['start_time'], 'duration': row['duration'], 'trainer': row['trainer'], 'description': row['description']} for row in data}
print(courseInfo)

date = sorted(courseInfo['name'], key = lambda item : datetime.strptime(item["start_date"],"%B %d %Y"))