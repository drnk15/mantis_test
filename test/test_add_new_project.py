from model.project import Project
import string
import random


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters
    r_str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return r_str


def test_add_new_project(app):
    soap_old_projects = app.soap.get_accessible_projects()
    project_name = random_project_name("pr_", 10)
    project = Project(name=project_name, status='development', inherit=True, view_state='public', description='sdfgadga')
    app.project.add_new_project(project)
    soap_old_projects.append(project)
    soap_new_projects = app.soap.get_accessible_projects()
    assert sorted(soap_old_projects, key=Project.id_or_max) == sorted(soap_new_projects, key=Project.id_or_max)
