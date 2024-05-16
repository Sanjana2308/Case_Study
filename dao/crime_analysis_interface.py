from abc import ABC, abstractmethod

class IcrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self, incident):
        pass

    @abstractmethod
    def update_incident_status(self):
        pass

    @abstractmethod
    def get_incidents_in_date_range(self):
        pass

    @abstractmethod
    def search_incidents(self):
        pass

    @abstractmethod
    def generate_incident_report(self):
        pass

    @abstractmethod
    def create_case(self):
        pass

    @abstractmethod
    def get_case_details(self):
        pass

    @abstractmethod
    def update_case_details(self):
        pass

    @abstractmethod
    def get_all_cases(self):
        pass