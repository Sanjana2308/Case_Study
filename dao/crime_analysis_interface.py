from abc import ABC, abstractmethod

class IcrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self, incidents):
        pass

    @abstractmethod
    def update_incident_status(self, incidentId, status):
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date, end_date):
        pass

    @abstractmethod
    def search_incidents(self, incident_type):
        pass

    @abstractmethod
    def generate_incident_report(self, report):
        pass

    @abstractmethod
    def create_case(self, cases):
        pass

    @abstractmethod
    def get_case_details(self, caseId):
        pass

    @abstractmethod
    def update_case_details(self):
        pass

    @abstractmethod
    def get_all_cases(self):
        pass