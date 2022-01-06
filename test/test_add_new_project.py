from model.project import Project


def test_add_new_project(app):
    app.session.login("administrator", "root")
    #old_projects = app.project.get_list()
    project = Project(name='new', status='в разработке', inherit=True, view_state='публичный', description='sdfgadga')
    app.project.add_new_project(project)
    #old_projects.apped(project)
    #new_projects = app.project.get_list()
    #assert old_projects == new_projects
