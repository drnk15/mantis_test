from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.check_for_test_project()
    old_projects = app.project.get_list()
    app.project.delete_random_project()
    new_projects = app.project.get_list()
    assert old_projects == new_projects