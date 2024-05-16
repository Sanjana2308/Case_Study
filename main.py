from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims
from dao.crime_analysis import CrimeAnalysisService

class MainMenu:
    crime_service = CrimeAnalysisService()

    def main_menu(self):
        self.crime_service.read_victims()

main = MainMenu()
main.main_menu()