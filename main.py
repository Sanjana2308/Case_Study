from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims
from dao.crime_analysis import CrimeAnalysisService

class MainMenu:
    crime_service = CrimeAnalysisService()

    def main_menu(self):
        while True:
            print("""
1. Create incident
2. Update ncident status
3. Get incidents in date range
4. Search incidents                                  
5. Generate incident report
6. Create case
7. Get case details
8. Update case details
9. Get a list of all cases
10. Exit
""")
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                continue

            elif choice == 2:
                continue

            elif choice == 3:
                continue

            elif choice == 4:
                continue

            elif choice == 5:
                continue

            elif choice == 6:
                continue

            elif choice == 7:
                continue

            elif choice == 8:
                continue

            elif choice == 9:
                continue

            elif choice == 10:
                break

            else:
                print("Please enter correct choice from menu!")

if __name__ == "__main__"
    main = MainMenu()
    main.main_menu()