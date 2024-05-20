class IncidentNumberNotFoundException(Exception):
    def __init__(self, incident_id):
        super().__init__(f"Incident with {incident_id} not found")

class CaseNumberNotFoundException(Exception):
    def __init__(self, CaseID):
        super().__init__(f"Case with ID {CaseID} is not Found")