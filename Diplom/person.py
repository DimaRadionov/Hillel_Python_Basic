from dateutil.relativedelta import relativedelta
import datetime


class Person:
    def __init__(self, first_name, last_name="", middle_name="", birth_date="", death_date="", gender=""):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def calculate_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.birth_date, "%d.%m.%Y").date()
        if self.death_date:
            death_date = datetime.datetime.strptime(self.death_date, "%d.%m.%Y").date()
            age = relativedelta(death_date, birth_date).years
        else:
            age = relativedelta(today, birth_date).years
        return age
