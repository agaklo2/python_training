from sys import maxsize

class Contact:

    def __init__(self, name=None, surname=None):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return "%s:%s" % (self.name, self.surname)

    def __eq__(self, other):
        return (self.surname is None or other.surname is None or self.surname == other.surname) and self.surname == other.surname

    def surname_or_max(self):
        if self.surname:
            return str(self.surname)
        else:
            return str(maxsize)