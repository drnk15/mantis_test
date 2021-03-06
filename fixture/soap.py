from suds.client import Client
from suds import WebFault
from suds.sudsobject import asdict
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + '/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_accessible_projects(self):
        client = Client(self.app.base_url + '/api/soap/mantisconnect.php?wsdl')
        try:
            response = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['user'],
                                                                      self.app.config['webadmin']['password'])
            result = []
            for item in response:
                item = asdict(item)
                project_id = item['id']
                name = item['name']
                status = asdict(item['status'])['name']
                enabled = item['enabled']
                view_state = asdict(item['view_state'])['name']
                if item['description'] is None:
                    description = ""
                else:
                    description = item['description']
                result.append(
                    Project(id=project_id, name=name, status=status, enabled=enabled, view_state=view_state,
                            description=description)
                )

            return list(result)
        except WebFault:
            return None
