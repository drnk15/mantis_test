from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def manage_proj_page_is_open(self):
        wd = self.app.wd
        return wd.current_url.endswith("/manage_proj_page.php")

    def open_manage_proj_page(self):
        wd = self.app.wd
        if not self.manage_proj_page_is_open():
            wd.find_element_by_css_selector("a[href$='/manage_overview_page.php']").click()
            wd.find_element_by_css_selector("a[href$='/manage_proj_page.php']").click()

    def add_new_project(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_xpath("//button[text()='Создать новый проект']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        wd.find_element_by_link_text("Продолжить").click()

    def count(self):
        wd = self.app.wd
        self.open_manage_proj_page()
        projects = wd.find_elements_by_css_selector("a[$href='manage_proj_edit_page.php?project_id=']")
        return len(projects)

    def check_for_test_project(self):
        if self.count == 0:
            self.add_new_project(Project(name='test'))

    def delete_random_project(self):
        pass

    def get_list(self):
        pass

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        wd.find_element_by_id("project-status").click()
        wd.find_element_by_xpath(f"//select[@id='project-status']/option[text()='{project.status}']").click()
        if not project.inherit:
            wd.find_element_by_xpath("//input[@id='project-inherit-global']/span").click()
        wd.find_element_by_id("project-view-state").click()
        wd.find_element_by_xpath(f"//select[@id='project-view-state']/option[text()='{project.view_state}']").click()
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.description)
