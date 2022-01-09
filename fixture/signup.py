import re


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("email-field").click()
        wd.find_element_by_id("email-field").send_keys(email)
        wd.find_element_by_css_selector("input[value='Signup']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        wd.get(url)

        wd.find_element_by_id("realname").click()
        wd.find_element_by_id("realname").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("password-confirm").click()
        wd.find_element_by_id("password-confirm").send_keys(password)
        wd.find_element_by_css_selector("button[type='submit']").click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)
