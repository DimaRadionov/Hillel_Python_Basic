from person import Person


class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search_person(self, query):
        results = []
        for person in self.people:
            if query.lower() in person.first_name.lower() or query.lower() in person.last_name.lower() or query.lower() in person.middle_name.lower():
                results.append(person)
        return results

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for person in self.people:
                file.write(f"{person.first_name},{person.last_name},{person.middle_name},{person.birth_date},{person.death_date},{person.gender}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                person = Person(*data)
                self.people.append(person)
