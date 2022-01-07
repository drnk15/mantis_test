class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector('input[name="username"]').click()
        wd.find_element_by_css_selector('input[name="username"]').send_keys(username)
        # в версии mantisbt-2.25.2 интерфейс логина отличается от показанного в занятии
        # поле ввода пароля выводится после подтверждения имени пользователя
        wd.find_element_by_css_selector('input[value="Вход"]').click()
        wd.find_element_by_css_selector('input[name="password"]').click()
        wd.find_element_by_css_selector('input[name="password"]').send_keys(password)
        wd.find_element_by_css_selector('input[value="Вход"]').click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('span[class="user-info"]')) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector('span[class="user-info"]').text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('span[class="user-info"]').click()
        wd.find_element_by_css_selector("a[href$='/logout_page.php']").click()
        wd.find_element_by_css_selector('input[id="username"]')

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
