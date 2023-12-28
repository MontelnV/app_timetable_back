from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Facultet, Course, Group

app = Flask(__name__)
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template('index.html', facultets=get_facultets())

@app.route('/courses/<int:facultet_id>')
def courses(facultet_id):
    return render_template('courses.html', courses=get_courses(facultet_id))

@app.route('/groups/<int:course_id>')
def groups(course_id):
    return render_template('groups.html', groups=get_groups(course_id))

@app.route('/group_details/<int:group_id>')
def group_details(group_id):
    group = get_group_details(group_id)
    return render_template('group_details.html', group=group)

@app.route('/get_group_data/<int:group_id>')
def get_group_data(group_id):
    # Получаем данные о группе по ее идентификатору
    group = get_group_details(group_id)
    return group.data  # Возвращаем только данные о группе


def get_facultets():
    session = Session()
    facultets = session.query(Facultet).all()
    session.close()
    return facultets

def get_group_details(group_id):
    session = Session()
    group = session.query(Group).filter_by(id=group_id).first()
    session.close()
    return group


def get_courses(facultet_id):
    session = Session()
    courses = session.query(Course).filter_by(facultet_id=facultet_id).all()
    session.close()
    return courses

def get_groups(course_id):
    session = Session()
    groups = session.query(Group).filter_by(course_id=course_id).all()
    session.close()
    return groups

if __name__ == '__main__':
    app.run()
