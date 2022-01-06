import random


def test_delete_random_project(app):
    app.session.login("administrator", "root")
    app.project.check_for_test_project()
    old_projects = app.project.get_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_list()
    old_projects[0:1] = []
    assert old_projects == new_projects
