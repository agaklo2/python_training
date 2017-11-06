class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        # come back to home card
        wd.find_element_by_link_text("home").click()
        # click add button
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surname)
        # submit
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()