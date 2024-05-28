from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims, Cases

from dao import CrimeAnalysisServiceImpl

from datetime import datetime

from tabulate import tabulate

class MainModule:
    crime_service = CrimeAnalysisServiceImpl()

    def incident_menu(self):
        
        while True:
            print("\n👇 Choose functionality for Incidents")
            print("""1. Create incident
2. Update incident status
3. Get incidents in date range
4. Search incidents by incident type
5. Search incident by Incident ID                                 
6. Print all incidents
7. Back to main menu
""")
            choice = int(input("Enter your choice: "))
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
                
                date = input("Enter date in the format YYYY-MM-DD: ")
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
                    print(f"✅Incident Created with ID: {created[0]}")
                else:
                    print("Could not create Incident❌")

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
                    print("Incident Status Updated successfully✅")
                else:
                    print("Could not update Status❌")

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

            # Search Incident by Incident ID
            elif choice == 5:
                incidentID = int(input("Enter incident ID: "))
                incidents = self.crime_service.get_incident_by_id(incidentID)
                head = ["Incident ID", "Incident Type", "Incident Date", "Longitude", "Latitude", "Description", "Status", "Victim ID", "Suspect ID"]
                print(tabulate(incidents, headers = head, tablefmt = "grid"))

            # Get a list of all Incidents
            elif choice == 6:
                incidents = self.crime_service.get_all_incidents()
                head = ["Incident ID", "Incident Type", "Incident Date", "Longitude", "Latitude", "Description", "Status", "Victim ID", "Suspect ID"]
                print(tabulate(incidents, headers = head, tablefmt = "grid"))

            # Back to main menu
            elif choice == 7:
                break
            else:
                print("⚠️  Please enter correct choice from menu!")

    def report_menu(self):

        
        while True:
            print("\n👇 Choose functionality for Reports")
            print("""
1. Generate incident report
2. Display incident report by Report ID
3. Display all reports
4. Back to main menu
""")
            choice = int(input("Enter your choice: "))
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
                

            # Display Incident Report
            elif choice == 2:
                report_id = int(input("Enter report ID: "))
                reports = self.crime_service.get_report(report_id)

                head = ["Report ID", "Incident ID", "Reporting Officer ID", "Report Date", "Details", "Status"]

                print(tabulate(reports, headers = head, tablefmt = "grid"))

            # Get a list of all reports
            elif choice == 3:
                reports = self.crime_service.get_all_reports()
                head = ["Report ID", "Incident ID", "Reporting Officer ID", "Report Date", "Details", "Status"]
                print(tabulate(reports, headers = head, tablefmt = "grid"))

            # Back to main menu
            elif choice == 4:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")

    def case_menu(self):


        while True:
            print("\n👇 Choose functionality for Cases")
            print("""1. Create case
2. Get case details
3. Update case details
4. Get a list of all cases
5. Back to main menu
""")
            choice = int(input("Enter your choice: "))
            print("_"*100+"\n")

            # Create case
            if choice == 1:
                description = input("Enter case description: ")
                incident_id = int(input("Enter incident id: "))

                new_case = Cases(description, incident_id)
                created = self.crime_service.create_case(new_case)
                if created:
                    print(f"✅New Case Created with CaseID: {created[0]}")
                else:
                    print("Couldn't create case❌")
                

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
                    print("Case details updated✅")
                else:
                    print("Could not update case details❌")

            # Get a list of all cases
            elif choice == 4:
                cases = self.crime_service.get_all_cases()

                head = ["Case ID", "Description", "Incident ID"]

                print(tabulate(cases, headers= head, tablefmt="grid"))

            # Back to main menu
            elif choice == 5:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")

    def evidence_menu(self):
        while True:
            print("\n👇 Choose functionality for Evidence")
            print("""
1. Add new evidence
2. Display evidence details by evidence ID
3. Display evidence details by incident ID
4. Get a list of all evidences
5. Back to main menu
""")
            choice = int(input("Enter your choice: "))
            print("_"*100+"\n")

            # Add new evidence
            if choice == 1:
                description = input("Enter description of evidence: ")
                location = input("Enter location of evidence: ")
                incident_id = int(input("Enter incident ID for evidence: "))
                new_evidence = Evidence(description, location, incident_id)
                evidence = self.crime_service.generate_evidence(new_evidence)
                
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidence, headers=head, tablefmt = "grid"))
                print("Evidence added Successfully✅")

            # Display evidence details by evidence ID
            elif choice == 2:
                evidenceID = int(input("Enter evidence ID: "))
                evidences = self.crime_service.get_evidence_by_evidence_id(evidenceID)
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidences, headers=head, tablefmt = "grid"))

            # Display evidence details by incident ID
            elif choice == 3:
                incidentID = int(input("Enter incident ID: "))
                evidences = self.crime_service.get_evidence_by_incident_id(incidentID)
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidences, headers=head, tablefmt = "grid"))

            # Display a list of all evidences
            elif choice == 4:
                evidences = self.crime_service.get_all_evidences()
                head = ["Evidence ID", "Description", "Location Found", "Incident ID"]
                print(tabulate(evidences, headers=head, tablefmt = "grid"))


            # Back to main menu
            elif choice == 5:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")

    def law_enforcement_agency_menu(self):
        while True:
            print("\n👇 Choose functionality for Law Enforcement Agency")
            print("""
1. Add new Agency
2. Display agency details by Agency ID
3. Display a list of all agencies 
4. Back to main menu
""")
            choice = int(input("Enter your choice: "))
            print("_"*100+"\n")

            # Add new agency
            if choice == 1:
                agency_name = input("Enter agency name: ")
                jurisdiction = input("Enter jurisdiction: ")
                contact_info = input("Enter contact information: ")
                incidentID = int(input("Enter Incident ID: "))
                new_agency = LawEnforcementAgency(agency_name, jurisdiction, contact_info, incidentID)
                agency = self.crime_service.create_law_enforcement_agency(new_agency)
                head = ["Agency ID", "Agency Name", "Jurisdiction", "Contact Information", "Incident ID"]
                print(tabulate(agency, headers= head, tablefmt="grid"))
                print("New agency added successfully✅")

            # Display agency details by Agency ID
            elif choice == 2:
                agencyID = int(input("Enter agency ID: "))
                agency = self.crime_service.get_law_enforcement_agency_by_agency_id(agencyID)
                head = ["Agency ID", "Agency Name", "Jurisdiction", "Contact Information", "Incident ID"]
                print(tabulate(agency, headers= head, tablefmt="grid"))

            # Display a list of all agencies
            elif choice == 3:
                agency = self.crime_service.get_all_law_enforcement_agencies()
                head = ["Agency ID", "Agency Name", "Jurisdiction", "Contact Information", "Incident ID"]
                print(tabulate(agency, headers= head, tablefmt="grid"))

            # Back to main menu
            elif choice == 4:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")

    def officer_menu(self):
        while True:
            print("\n👇 Choose functionality for Officers")
            print("""
1. Add new Officer
2. Display officer details by Officer ID
3. Display a list of all Officers
4. Back to main menu
""")
            choice = int(input("Enter your choice: "))
            print("_"*100+"\n")

            # Add new officer
            if choice == 1:
                firstname = input("Enter first name: ")
                lastname = input("Enter lastname: ")
                badge_number = int(input("Enter badge number: "))
                rank = input("Enter rank of officer: ")
                contact_info = input("Enter contact information: ")
                agency_id = int(input("Enter agency ID of agency of officer: "))
                new_officer = Officers(firstname, lastname, badge_number, rank, contact_info, agency_id)
                officer = self.crime_service.create_officer(new_officer)
                head = ["Officer ID", "First Name", "Last Name", "Badge Number", "Rank", "Contact Information", "Agency ID"]
                print(tabulate(officer, headers=head, tablefmt="grid"))
                print("New officer added successfully✅")

            # Display officer details by Officer ID
            elif choice == 2:
                officerID = int(input("Enter Officer ID: "))
                officer = self.crime_service.get_officer_by_officer_id(officerID)
                head = ["Officer ID", "First Name", "Last Name", "Badge Number", "Rank", "Contact Information", "Agency ID"]
                print(tabulate(officer, headers=head, tablefmt="grid"))

            # Display a list of all officers
            elif choice == 3:
                officers = self.crime_service.get_all_officers()
                head = ["Officer ID", "First Name", "Last Name", "Badge Number", "Rank", "Contact Information", "Agency ID"]
                print(tabulate(officers, headers=head, tablefmt="grid"))


            # Back to main menu
            elif choice == 4:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")

    def suspect_menu(self):
        while True:
            print("\n👇 Choose functionality for Suspects")
            print("""
1. Add new Suspect
2. Display suspect details by Suspect ID
3. Display a list of all Suspects
4. Back to main menu
""")
            choice = int(input("Enter your choice: "))
            print("_"*100+"\n")

            # Add new suspect
            if choice == 1:
                firstname = input("Enter first name: ")
                lastname = input("Enter lastname: ")
                date = input("Enter date of birth in the format YYYY-MM-DD: ")
                dob = datetime.strptime(date, "%Y-%m-%d")
                gender = input("Enter gender: ")
                contact_info = input("Enter contact information: ")
                new_suspect = Suspects(firstname, lastname, dob, gender, contact_info)
                suspect = self.crime_service.create_suspect(new_suspect)
                head = ["Suspect ID", "First Name", "Last Name", "Date of Birth", "Gender", "Contact Information"]
                print(tabulate(suspect, headers=head, tablefmt="grid"))
                print("New suspect added successfully✅")

            # Display suspect details by Suspect ID
            elif choice == 2:
                suspectID = int(input("Enter suspect ID: "))
                suspect = self.crime_service.get_suspect_by_id(suspectID)
                head = ["Suspect ID", "First Name", "Last Name", "Date of Birth", "Gender", "Contact Information"]
                print(tabulate(suspect, headers=head, tablefmt="grid"))

            # Display a list of all Suspects
            elif choice == 3:
                suspect = self.crime_service.get_all_suspects()
                head = ["Suspect ID", "First Name", "Last Name", "Date of Birth", "Gender", "Contact Information"]
                print(tabulate(suspect, headers=head, tablefmt="grid"))

            # Back to main menu
            elif choice == 4:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")

    def victim_menu(self):
        while True:
            print("\n👇 Choose functionality for Victims")
            print("""
1. Add new Victim
2. Display Victim details by Victim ID
3. Display a list of all Victims
4. Back to main menu
""")
            choice = int(input("Enter your choice: "))
            print("_"*100+"\n")

            # Add new victim
            if choice == 1:
                firstname = input("Enter first name: ")
                lastname = input("Enter lastname: ")
                date = input("Enter date of birth in the format YYYY-MM-DD: ")
                dob = datetime.strptime(date, "%Y-%m-%d")
                gender = input("Enter gender: ")
                contact_info = input("Enter contact information: ")
                new_victim = Victims(firstname, lastname, dob, gender, contact_info)
                victim = self.crime_service.create_victim(new_victim)
                head = ["Victim ID", "First Name", "Last Name", "Date of Birth", "Gender", "Contact Information"]
                print(tabulate(victim, headers=head, tablefmt="grid"))
                print("New victim added successfully✅")

            # Display Victim details by Victim ID
            elif choice == 2:
                victimID = int(input("Enter victim ID: "))
                victim = self.crime_service.get_victim_by_id(victimID)
                head = ["Victim ID", "First Name", "Last Name", "Date of Birth", "Gender", "Contact Information"]
                print(tabulate(victim, headers=head, tablefmt="grid"))

            # Display a list of all Victims
            elif choice == 3:
                victim = self.crime_service.get_all_victims()
                head = ["Victim ID", "First Name", "Last Name", "Date of Birth", "Gender", "Contact Information"]
                print(tabulate(victim, headers=head, tablefmt="grid"))

            # Back to main menu
            elif choice == 4:
                break

            else:
                print("⚠️  Please enter correct choice from menu!")



def main():
    main_menu = MainModule()

    while True:
        print("_"*100+"\n")
        print("👇 Choose your preference from the below options")

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
        choice = int(input("Enter your choice: "))
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
            print("-"*40+"👋"*10+"-"*40)
            break

        else:
            print("⚠️  Please enter correct choice from menu!")

if __name__ == "__main__":
    print("_"*100+"\n")
    print("😊 Welcome to Crime Analysis and Reporting System!😊")
    main()