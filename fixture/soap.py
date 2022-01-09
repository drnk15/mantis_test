from suds.client import Client
from suds import WebFault
from suds.sudsobject import asdict
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client('http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl')

    def can_login(self, username, password):
        client = self.client
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_accessible_projects(self, username, password):
        client = self.client
        try:
            response = client.service.mc_projects_get_user_accessible(username, password)
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
