class IncidentNumberNotFoundException(Exception):
    def __init__(self, incident_id):
        super().__init__(f"Incident with ID {incident_id} not found")

class CaseNumberNotFoundException(Exception):
    def __init__(self, caseID):
        super().__init__(f"Case with ID {caseID} is not found")

class ReportNumberNotFoundException(Exception):
    def __init__(self, reportID):
        super().__init__(f"Report with ID {reportID} is not found")

class EvidenceNumberNotFoundException(Exception):
    def __init__(self, evidenceID):
        super().__init__(f"Report with ID {evidenceID} is not found")

class LawEnforcementAgencyNumberNotFoundException(Exception):
    def __init__(self, agencyID):
        super().__init__(f"Report with ID {agencyID} is not found")

class OfficerNumberNotFoundException(Exception):
    def __init__(self, officerID):
        super().__init__(f"Officer with ID {officerID} is not found")

class SuspectNumberNotFoundException(Exception):
    def __init__(self, suspectID):
        super().__init__(f"Suspect with ID {suspectID} is not found")

class VictimNumberNotFoundException(Exception):
    def __init__(self, victimID):
        super().__init__(f"Victim with ID {victimID} is not found")