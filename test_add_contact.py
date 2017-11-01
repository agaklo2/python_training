# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_card(wd)
        self.login(wd,  username="admin", password="secret")
        self.add_new_contact(wd,  Contact(name="Agata", surname="Kłopotowska"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_card(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact(name="", surname=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self, wd, contact):
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

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_card(self, wd):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_css_selector("html").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
