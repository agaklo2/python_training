import mysql.connector
from model.group import Group
#from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_group_by_id(self, group_id):
        #list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM `group_list` WHERE `group_id` ="+group_id)
            for row in cursor:
                (id, name, header, footer) = row
                selected_group = Group(id=str(id), name=name, header=header, footer=footer)
        finally:
            cursor.close()
        return selected_group


#    def get_contact_list(self):
#        list = []
#        cursor = self.connection.cursor()
#        try:
#            cursor.execute("select id, firstname, lastname, address from addressbook")
#            for row in cursor:
#                (id, firstname, lastname, address) = row
#                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address))
#        finally:
#            cursor.close()
#        return list



    def destroy(self):
        self.connection.close()


