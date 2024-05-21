from datetime import datetime, timedelta
from sqlalchemy import (CheckConstraint, Column, 
    CHAR, Date, Integer, LargeBinary, String, Numeric, Boolean, ForeignKey, Time, 
    func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import time
import pytz

Base = declarative_base()


#Ключи========================================================================>
class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(length=30), unique=True, nullable=False)
    name_en = Column(String(length=30), unique=True, nullable=False)
    letter_code = Column(CHAR(length=2), unique=True, nullable=False)
    digit_code = Column(String(length=3), unique=True, nullable=False)

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30), unique=True, nullable=False)
    is_recognized = Column(Boolean, default=True, nullable=False)
    country_id = Column(Integer, ForeignKey(Country.id), nullable=False)

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    title = Column(CHAR(length=11), unique=True, nullable=False)

class Gender(Base):
    __tablename__ = "gender"

    id = Column(Integer, primary_key=True)
    title = Column(CHAR(length=7), unique=True, nullable=False)

class Direction(Base):
    __tablename__ = "direction"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=30), unique=True, nullable=False)

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=30), unique=True, nullable=False)

#Основные модели========================================================================>
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey(Role.id), nullable=False)
    email = Column(String(length=30), unique=True, nullable=False)
    password = Column(String(length=20), nullable=False)
    surname = Column(String(length=30), nullable=False)
    name = Column(String(length=30), nullable=False)
    patronymic = Column(String(length=30), nullable=True)
    gender_id = Column(Integer, ForeignKey(Gender.id), nullable=False)
    birth_date = Column(Date, default=datetime.now(pytz.timezone("Europe/Moscow")) - timedelta(days=18*365), nullable=False)
    country_id = Column(Integer, ForeignKey(Country.id), nullable=False)
    phone_number = Column(String(length=20), unique=True, nullable=False)
    direction_id = Column(Integer, ForeignKey(Direction.id), nullable=True)
    event_id = Column(Integer, ForeignKey(Event.id), nullable=True)

class Meet(Base):
    __tablename__ = "meet"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True, nullable=False)
    date = Column(Date, default=datetime.now(pytz.timezone("Europe/Moscow")) + timedelta(days=7), nullable=False)
    days_count = Column(Numeric(precision=2), nullable=False)
    city_id = Column(Integer, ForeignKey(City.id), nullable=False)
    direction_id = Column(Integer, ForeignKey(Direction.id))
    winner_id = Column(Integer, ForeignKey(User.id), nullable=False)
    photo = Column(LargeBinary, nullable=False)

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30), unique=True, nullable=False)
    meet_id = Column(Integer, ForeignKey(Meet.id), nullable=False)
    day_number = Column(Numeric(precision=1), nullable=False)
    time = Column(Time, default=time(hour=9), nullable=False)
    moderator_id = Column(Integer, ForeignKey(User.id), nullable=False)

class ActivityJury(Base):
    __tablename__ = "activity_jury"

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey(Activity.id), nullable=False)
    jury_id = Column(Integer, ForeignKey(User.id), nullable=False)
    #Тут должно быть нечто




