import datetime


class UserAlreadyExists(Exception):
    pass

class Person:

    def __init__(self, name, id = None, amount = None, jobs = None):
        self.name = name
        self.id = id if id else hash(name)
        self.amount = amount if amount else 0
        self.jobs = jobs if jobs else []

    def to_dict(self):
        return {'name': self.name, 'id': self.id, 'amount': self.amount, 'jobs': self.jobs}

class Job():

    def __init__(self, person, job, amount, date):
        self.person = person
        self.job = job
        self.amount = amount
        self.date = date

    def __dict__(self):
        return {'person': self.person, 'job': self.job, 'amount': self.amount, 'date': self.date}