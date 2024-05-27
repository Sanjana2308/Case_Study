class IncidentNumberNotFoundException(Exception):
    def __init__(self, incident_id):
        super().__init__(f"Incident with {incident_id} not found")

class CaseNumberNotFoundException(Exception):
    def __init__(self, caseID):
        super().__init__(f"Case with {caseID} is not found")

class ReportNumberNotFoundException(Exception):
    def __init__(self, reportID):
        super().__init__(f"Report with {reportID} is not found")

class EvidenceNumberNotFoundException(Exception):
    def __init__(self, evidenceID):
        super().__init__(f"Report with {evidenceID} is not found")

class LawEnforcementAgencyNumberNotFoundException(Exception):
    def __init__(self, agencyID):
        super().__init__(f"Report with {agencyID} is not found")