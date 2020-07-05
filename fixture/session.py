from selenium.webdriver.common.by import By

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.driver = self.app.driver
        self.app.open_home_page()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_elements(By.CSS_SELECTOR, ".btn-success").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_elements(By.CSS_SELECTOR, ".btn-success").click()

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".user-block .link-content").click()
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()

    def ensure_logout(self):
        self.driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        self.driver = self.app.driver
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".user-block .link-content")) > 0

    def is_logged_in_as(self, username):
        self.driver = self.app.driver
        return self.driver.find_element(By.XPATH, "//b[contains(.,'Anastasiia')]").text == "Anastasiia"

    def ensure_login(self, username, password):
        self.driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

