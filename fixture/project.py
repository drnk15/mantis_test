from model.project import Project
import re


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
        wd.find_element_by_xpath("//button[text()='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.projects_cache = None

    def count(self):
        wd = self.app.wd
        self.open_manage_proj_page()
        projects = wd.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr")
        return len(projects)

    def check_for_test_project(self):
        if self.count() == 0:
            self.add_new_project(Project(name='test', status='development', inherit=True, view_state='public',
                                         description='sdfgadga'))

    def delete_project(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_xpath(f"//td/a[text()='{project.name}']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.projects_cache = None

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

    projects_cache = None

    def get_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_manage_proj_page()
            self.projects_cache = []
            table = wd.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr")
            for element in table:
                project_id = re.findall(r'\d+', element.find_element_by_xpath("./td[1]/a").get_attribute("href"))[-1]
                name = element.find_element_by_xpath("./td[1]/a").text
                status = element.find_element_by_xpath("./td[2]").text
                if len(element.find_elements_by_xpath("./td[3]/i[@class='fa fa-check fa-lg']")) == 1:
                    enabled = True
                else:
                    enabled = False
                view_state = element.find_element_by_xpath("./td[4]").text
                description = element.find_element_by_xpath("./td[5]").text
                self.projects_cache.append(
                    Project(id=project_id, name=name, status=status, enabled=enabled, view_state=view_state,
                            description=description)
                )
        return list(self.projects_cache)

