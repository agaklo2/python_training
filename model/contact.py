class Contact:

    def __init__(self, name=None, surname=None):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return "%s:%s" % (self.name, self.surname)

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname
