from model.project import Project


def test_delete_first_project(app):
    app.project.check_for_test_project()
    sorted_soap_old_projects = sorted(app.soap.get_accessible_projects("administrator", "root"), key=Project.id_or_max)
    project = sorted_soap_old_projects[0]
    app.project.delete_project(project)
    soap_new_projects = app.soap.get_accessible_projects("administrator", "root")
    sorted_soap_old_projects[0:1] = []
    assert sorted_soap_old_projects == sorted(soap_new_projects, key=Project.id_or_max)
