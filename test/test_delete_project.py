def test_delete_first_project(app):
    app.project.check_for_test_project()
    old_projects = app.project.get_list()
    project = old_projects[0]
    app.project.delete_project(project)
    new_projects = app.project.get_list()
    old_projects[0:1] = []
    assert old_projects == new_projects
