from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Facultet(Base):
    __tablename__ = 'facultets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', back_populates='facultet')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    facultet_id = Column(Integer, ForeignKey('facultets.id'))
    facultet = relationship('Facultet', back_populates='courses')
    groups = relationship('Group', back_populates='course')

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='groups')