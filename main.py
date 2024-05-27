from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims, Cases

from dao import CrimeAnalysisServiceImpl

from datetime import datetime

from tabulate import tabulate

class MainModule:
    crime_service = CrimeAnalysisServiceImpl()

    def incident_menu(self):
        
        while True:
            print("\nChoose your preference from the below options!!")
            print("""1. Create incident
2. Update incident status
3. Get incidents in date range
4. Search incidents by incident type
5. Search incident by Incident ID                                 
6. Back to main menu
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
                location_longitude = float(input("Enter longitude value of location: "))
                location_latitude = float(input("Enter latitude value of location: "))
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

            # Update Incident Status
            elif choice == 2:
                incident_id = int(input("Enter Incident ID: "))
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
                updated = self.crime_service.update_incident_status(incident_id, status)
                if updated:
                    print("Incident Status Updated successfully")
                else:
                    print("Could not update Status")

            # Get incidents in date range
            elif choice == 3:
                incident_start_date = input("Enter start date in the format YYYY-MM-DD: ")
                
                incident_end_date = input("Enter end date in the format YYYY-MM-DD: ")
                
                incidents = self.crime_service.get_incidents_in_date_range(incident_start_date, incident_end_date)

                head = ["Incident ID", "Incident Type", "Incident Date", "Longitude", "Latitude", "Description", "Status", "Victim ID", "Suspect ID"]
                
                print(tabulate(incidents, headers = head, tablefmt = "grid"))


            # Search Incidents
            elif choice == 4:
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

                incidents = self.crime_service.search_incidents(incident_type)

                head = ["Incident ID", "Incident Type", "Incident Date", "Longitude", "Latitude", "Description", "Status", "Victim ID", "Suspect ID"]
                
                print(tabulate(incidents, headers = head, tablefmt = "grid"))

            # Back to main menu
            elif choice == 6:
                break

            else:
                print("Please enter correct choice from menu!")

    def report_menu(self):

        
        while True:
            print("\nChoose your preference from the below options!!")
            print("""
1. Generate incident report
2. Display incident report
3. Exit
""")
            choice = int(input("Please choose from above options: "))

            # Generate Incident Report
            if choice == 1:
                incident_id = int(input("Enter incident id: "))
                reporting_officer = input("Enter reporting officer: ")
                report_date = input("Enter date in the format YYYY-MM-DD: ")
                report_details = input("Enter report details: ")
                status = input("Enter status: ")
                new_report = Reports(incident_id, reporting_officer, report_date, report_details, status)
                report = self.crime_service.generate_incident_report(new_report)

                head = ["Report ID", "Incident ID", "Reporting Officer ID", "Report Date", "Details", "Status"]

                print(tabulate(report, headers = head, tablefmt = "grid"))

            elif choice == 2:
                report_id = int(input("Enter report ID: "))
                reports = self.crime_service.get_report(report_id)

                head = ["Report ID", "Incident ID", "Reporting Officer ID", "Report Date", "Details", "Status"]

                print(tabulate(reports, headers = head, tablefmt = "grid"))

            elif choice == 3:
                break

            else:
                print("Please enter correct choice from menu!")

    def case_menu(self):


        while True:
            print("\nChoose your preference from the below options!!")
            print("""1. Create case
2. Get case details
3. Update case details
4. Get a list of all cases
5. Back to main menu
""")
            choice = int(input("Please choose from above options: "))

            # Create case
            if choice == 1:
                description = input("Enter case description: ")
                incident_id = int(input("Enter incident id: "))

                new_case = Cases(description, incident_id)
                created = self.crime_service.create_case(new_case)
                if created:
                    print("New Case Created")
                else:
                    print("Couldn't create case")

            # Get case details
            elif choice == 2:
                case_id = int(input("Enter caseId: "))
                cases = self.crime_service.get_case_details(case_id)
                
                head = ["Case ID", "Description", "Incident ID"]

                print(tabulate(cases, headers= head, tablefmt="grid"))

            # Update case details
            elif choice == 3:
                case_id = int(input("Enter case ID to be updated: "))
                description = input("Enter description of case: ")
                updated = self.crime_service.update_case_details(case_id, description)
                if updated:
                    print("Case details updated")
                else:
                    print("Could not update case details")

            # Get a list of all cases
            elif choice == 4:
                cases = self.crime_service.get_all_cases()
                
                head = ["Case ID", "Description", "Incident ID"]

                print(tabulate(cases, headers= head, tablefmt="grid"))

            elif choice == 5:
                break

            else:
                print("Please enter correct choice from menu!")

    

def main():
    main_menu = MainModule()

    while True:
        print("_"*100+"\n")
        print("Choose your preference from the below options!!")

        print("""1. Incident Management
2. Report Management
3. Case Management
4. Exit
""")
        choice = int(input("Please choose from above options: "))
        print("_"*100+"\n")

        if choice == 1:
            
            main_menu.incident_menu()

        elif choice == 2:
            
            main_menu.report_menu()

        elif choice == 3:
            
            main_menu.case_menu()

        elif choice == 4:
            main_menu.crime_service.close()
            break

        else:
            print("Please enter correct choice from menu!")

        

if __name__ == "__main__":
    print("_"*100+"\n")
    print("Welcome to Crime Analysis and Reporting System!")
    main()