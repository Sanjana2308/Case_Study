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
            print("_"*100+"\n")
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


            # Search Incidents by incident type
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

            elif choice == 5:
                incidentID = int(input("Enter incident ID: "))
                incidents = self.crime_service.get_incident_by_id(incidentID)
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
            print("_"*100+"\n")
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
            print("_"*100+"\n")
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

    def evidence_menu(self):
        while True:
            print("\nChoose your preference from the below options!!")
            print("""
1. Generate evidence
2. Display evidence details by evidence ID
3. Display evidence details by incident ID
4. Back to main menu
""")
            choice = int(input("Please choose from above options: "))
            print("_"*100+"\n")
            if choice == 1:
                description = input("Enter description of evidence: ")
                location = input("Enter location of evidence: ")
                incident_id = int(input("Enter incident ID for evidence: "))
                new_evidence = Evidence(description, location, incident_id)
                evidence = self.crime_service.generate_evidence(new_evidence)
                
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidence, headers=head, tablefmt = "grid"))

            elif choice == 2:
                evidenceID = int(input("Enter evidence ID: "))
                evidences = self.crime_service.get_evidence_by_evidence_id(evidenceID)
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidences, headers=head, tablefmt = "grid"))

            elif choice == 3:
                incidentID = int(input("Enter incident ID: "))
                evidences = self.crime_service.get_evidence_by_incident_id(incidentID)
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidences, headers=head, tablefmt = "grid"))

            elif choice == 4:
                break

            else:
                print("Please enter correct choice from menu!")

    def law_enforcement_agency_menu(self):
        while True:
            print("\nChoose your preference from the below options!!")
            print("""
1. Generate Agency
2. Display agency details by Agency ID
3. Back to main menu
""")
            choice = int(input("Please choose from above options: "))
            print("_"*100+"\n")
            if choice == 1:
                agency_name = input("Enter agency name: ")
                jurisdiction = input("Enter jurisdiction of agency: ")
                contact_info = input("Enter contact information: ")
                officerID = int(input("Enter Officer ID: "))
                new_agency = LawEnforcementAgency(agency_name, jurisdiction, contact_info, officerID)
                agency = self.crime_service.create_law_enforcement_agency(new_agency)
                head = ["Agency ID", "Agency Name", "Jurisdiction", "Contact Information", "Officer ID"]
                print(tabulate(agency, headers= head, tablefmt="grid"))

            elif choice == 2:
                agencyID = int(input("Enter agency ID: "))
                agency = self.crime_service.get_law_enforcement_agency_by_agency_id(agencyID)
                head = ["Agency ID", "Agency Name", "Jurisdiction", "Contact Information", "Officer ID"]
                print(tabulate(agency, headers= head, tablefmt="grid"))

            elif choice == 3:
                break

            else:
                print("Please enter correct choice from menu!")

    def officer_menu(self):
        pass

    def suspect_menu(self):
        pass

    def victim_menu(self):
        pass 

    

def main():
    main_menu = MainModule()

    while True:
        print("_"*100+"\n")
        print("Choose your preference from the below options!!")

        print("""1. Incident Management
2. Report Management
3. Case Management
4. Evidence Management
5. Law Enforcement Agency Management
6. Officer Management
7. Suspect Management
8. Victim Management
9. Exit
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
            
            main_menu.evidence_menu()

        elif choice == 5:
            
            main_menu.law_enforcement_agency_menu()

        elif choice == 6:

            main_menu.officer_menu()

        elif choice == 7:

            main_menu.suspect_menu()

        elif choice == 8:

            main_menu.victim_menu()

        elif choice == 9:
            main_menu.crime_service.close()
            break

        else:
            print("Please enter correct choice from menu!")

        

if __name__ == "__main__":
    print("_"*100+"\n")
    print("Welcome to Crime Analysis and Reporting System!")
    main()