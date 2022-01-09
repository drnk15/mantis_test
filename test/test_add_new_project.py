from model.project import Project


def test_add_new_project(app):
    old_projects = app.project.get_list()
    project = Project(name='azxcv', status='development', inherit=True, view_state='public', description='sdfgadga')
    app.project.add_new_project(project)
    old_projects.append(project)
    new_projects = app.project.get_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
