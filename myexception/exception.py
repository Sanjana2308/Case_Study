class IncidentNumberNotFoundException(Exception):
    def __init__(self, incident_id):
        super().__init__(f"Incident with {incident_id} not found")

class CaseNumberNotFoundException(Exception):
    def __init__(self, caseID):
        super().__init__(f"Case with {caseID} is not found")

class ReportNumberNotFoundException(Exception):
    def __init__(self, reportID):
        super().__init__(f"Report with {reportID} is not found")