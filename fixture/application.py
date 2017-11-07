from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper
from fixture.contact_helper import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_home_card(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_css_selector("html").click()



    def destroy(self):
        self.wd.quit()

