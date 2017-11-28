from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        # click add button
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_card()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_card()
        self.choose_editing_contact_by_index(index)
        # modify contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def choose_editing_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_card()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_card()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
#                all_phones = cells[5].text.splitlines()

                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
#                                                  homephone=all_phones[0], mobilephone=all_phones[1],
#                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)

#    def get_contact_info_from_edit_page(self, index):
#        wd = self.app.wd
#        self.choose_editing_contact_by_index(index)
#        firstname = wd.find_element_by_name("firstname").get_attribute("value")
#        lastname = wd.find_element_by_name("lastname").get_attribute("value")
#        id = wd.find_element_by_name("id").get_attribute("value")
#        homephone = wd.find_element_by_name("home").get_attribute("value")
#        workphone = wd.find_element_by_name("work").get_attribute("value")
#        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
#        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
#        return Contact(firstname=firstname, lastname=lastname, id=id,
#                       homephone=homephone, mobilephone=mobilephone,
#                       workphone=workphone, secondaryphone=secondaryphone)