from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims

from dao.crime_analysis import CrimeAnalysisServiceImpl

from datetime import datetime

class MainModule:
    crime_service = CrimeAnalysisServiceImpl()

    def main_menu(self):
        while True:
            print("""
1. Create incident
2. Update incident status
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

            # Create incident
            if choice == 1:
                print("""
Incident type: 
1. Robbery
2. Homicide
3. Theft""")
                choice = int(input("Enter incident type: "))

                while True:
                    if choice == 1:
                        incident_type = "Robbery"
                        break
                    elif choice == 2:
                        incident_type = "Homicide"
                        break
                    elif choice == 3:
                        incident_type = "Theft"
                        break
                    else:
                        break
                print(incident_type)
                
                date = input("Enter a date in the format YYYY-MM-DD: ")
                incident_date = datetime.strptime(date, "%Y-%m-%d")
                location_longitude = float(input("""Enter longitude value of location
(max 8 decimal values allowed and integral part with 2 places): """))
                location_latitude = float(input("""Enter latitude value of location
(max 8 decimal values allowed and integral part with 2 values): """))
                description = input("Enter description of incident: ")
                
                print("""
Status type: 
1. Open
2. Closed
3. Under Investigation""")
                choice = int(input("Enter status of incident: "))

                while True:
                    if choice == 1:
                        status = "Open"
                        break
                    elif choice == 2:
                        status = "Closed"
                        break
                    elif choice == 3:
                        status = "Under Investigation"
                        break
                    else:
                        break
                print(status)
                victim_id = int(input("Enter victim id: "))
                suspect_id = int(input("Enter suspect id: "))
                new_incident = Incidents(incident_type, incident_date, location_longitude, location_latitude, description, status, victim_id, suspect_id)
                created = self.crime_service.create_incident(new_incident)
                if created:
                    print("Incident Created")
                else:
                    print("Could not create Incident")




                

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

if __name__ == "__main__":
    main = MainModule()
    main.main_menu()