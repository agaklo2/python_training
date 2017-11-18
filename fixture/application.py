from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper
from fixture.contact_helper import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_groups_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.get("http://localhost/addressbook/group.php")

    def open_home_card(self):
        wd = self.wd
        if not (wd.current_url.endswith("/adressbook/") and len(wd.find_elements_by_id("MassCB")) > 0):
            wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()

