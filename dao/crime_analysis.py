from util.DBConnection import DBConnection

from .crime_analysis_interface import IcrimeAnalysisService

from myexception.exception import IncidentNumberNotFoundException, CaseNumberNotFoundException, ReportNumberNotFoundException, EvidenceNumberNotFoundException, LawEnforcementAgencyNumberNotFoundException, OfficerNumberNotFoundException, SuspectNumberNotFoundException, VictimNumberNotFoundException

class CrimeAnalysisServiceImpl(DBConnection, IcrimeAnalysisService): 


    # Incident Management
    def create_incident(self, incidents):
        
        try:
            self.cursor.execute("""INSERT INTO Incidents(IncidentType, IncidentDate, Location_Longitude, Location_Latitude, Description, Status, VictimID, SuspectID) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                                    (incidents.incident_type, incidents.incident_date, incidents.location_latitude, incidents.location_longitude, incidents.description, incidents.status, incidents.victim_id, incidents.suspect_id))
            self.connection.commit()
            self.cursor.execute("""
                                select TOP 1 IncidentID
                                from Incidents
                                order by IncidentID DESC
                                """)
            incident_id = self.cursor.fetchone()
            return incident_id
        except Exception as e:
            print(e)
            return None

    def update_incident_status(self, incidentId, status):
        try:
            self.cursor.execute(
                """
                Update Incidents
                Set Status = ?
                where incidentId = ?
                """,
                (status, incidentId))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return None

    def get_incidents_in_date_range(self, start_date, end_date):
        try:
            self.cursor.execute(
                """
                select * 
                from Incidents
                where IncidentDate BETWEEN
                ? AND ?
                """,
                (start_date, end_date))
            
            incidents = self.cursor.fetchall()
            return incidents

        except Exception as e:
            print(e)

    def search_incidents(self, incident_type):
        try:
            self.cursor.execute(
                """
                select * from Incidents where incidentType IN (?)
                """,
                (incident_type)
                )
            incidents = self.cursor.fetchall()
            return incidents
        
        except Exception as e:
            print(e)

    def get_incident_by_id(self, incidentID):
        try:
            self.cursor.execute("""
                                select * 
                                from Incidents 
                                where IncidentID = ?
                                """,
                                (incidentID))
            incidents = self.cursor.fetchall()
            if len(incidents) == 0:
                raise IncidentNumberNotFoundException
            else:
                return incidents
        
        except Exception as e:
            print("⚠️Oops error happened!!",e)

    def get_all_incidents(self):
        try:
            self.cursor.execute("""
                                select *
                                from Incidents
                                """)
            incidents = self.cursor.fetchall()
            return incidents

        except Exception as e:
            print(e)

    # Report Management
    def generate_incident_report(self, report):
        try:
            self.cursor.execute(
                """
                INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status)
                VALUES (?, ?, ?, ?, ?)
                """,
                (report.incident_id, report.reporting_officer, report.report_date, report.report_details, report.status)
                )
            self.connection.commit()
            print("Report Generated✅")
            self.cursor.execute("""
                                SELECT TOP 1 * FROM Reports ORDER BY ReportID DESC;
                                """
                                )
            reports = self.cursor.fetchall()
            return reports

        except Exception as e:
            print(e)

    def get_report(self, reportID):
        try:
            self.cursor.execute("""
                                select * 
                                from Reports 
                                where ReportID = ?
                                """,
                                (reportID))
            reports = self.cursor.fetchall()

            if len(reports) == 0:
                raise ReportNumberNotFoundException
            else:
                return reports

        except Exception as e:
            print("⚠️Oops error happened: ",e)

    def get_all_reports(self):
        try:
            self.cursor.execute("""
                                select * 
                                from Reports
                                """)
            reports = self.cursor.fetchall()
            return reports
        except Exception as e:
            print(e)

    # Case Management
    def create_case(self, cases):
        try:
            self.cursor.execute("""
                                INSERT INTO Cases (CaseDescription, IncidentID)
                                VALUES
                                (?, ?)
                                """,
                                (cases.description, cases.incident_id)
                                )
            self.connection.commit()
            return True
        except Exception as e:
            print(e)

    def get_case_details(self, caseId):
        try:
            self.cursor.execute("""
                                select * from Cases where CaseID = ?
                                """,
                                (caseId)
                                )
            cases = self.cursor.fetchall()
            if len(cases) == 0:
                raise CaseNumberNotFoundException
            else:
                return cases
        except Exception as e:
            print("⚠️Oops error happened: ",e)
    
    def update_case_details(self, caseId, description):
        try:
            self.cursor.execute("""
                                Update Cases 
                                Set CaseDescription = ?
                                where CaseID = ?
                                """,
                                (description, caseId)
                                )
            self.connection.commit()
            return True
        except Exception as e:
            print(e)  

    def get_all_cases(self):
        try:
            self.cursor.execute("select * from Cases")
            cases = self.cursor.fetchall()
            return cases
        
        except Exception as e:
            print(e)
          

    # Evidence Management
    def generate_evidence(self, evidence):
        try:
            self.cursor.execute(
                """
                INSERT INTO Evidence(Description, LocationFound, IncidentID)
                VALUES
                (?, ?, ?)
                """,
                (evidence.description, evidence.location_found, evidence.incident_id)
                )
            self.connection.commit()
            print("Evidence Generated✅")
            self.cursor.execute("""
                                SELECT TOP 1 *
                                FROM Evidence 
                                ORDER BY EvidenceID DESC;
                                """
                                )
            evidences = self.cursor.fetchall()
            return evidences
        
        except Exception as e:
            print(e)

    def get_evidence_by_evidence_id(self, evidenceID):
        try:
            self.cursor.execute("""
                                select * 
                                from Evidence
                                where EvidenceID = ?
                                """,
                                (evidenceID))
            evidence = self.cursor.fetchall()
            if len(evidence) == 0:
                raise EvidenceNumberNotFoundException
            else:
                return evidence
            
        except Exception as e:
            print("⚠️Oops error occured: ",e)

    def get_evidence_by_incident_id(self, incidentID):
        try:
            self.cursor.execute("""
                                select * 
                                from Evidence
                                where IncidentID = ?
                                """,
                                (incidentID))
            evidence = self.cursor.fetchall()
            if len(evidence) == 0:
                raise EvidenceNumberNotFoundException
            else:
                return evidence
            
        except Exception as e:
            print(e)

    def get_all_evidences(self):
        try:
            self.cursor.execute("""
                                select * 
                                from Evidence
                                """)
            evidence = self.cursor.fetchall()
            return evidence
        
        except Exception as e:
            print(e)

    # Law Enforcement Agency Management
    def create_law_enforcement_agency(self, agency):
        try:
            self.cursor.execute("""
                                INSERT INTO LawEnforcementAgency (AgencyName, Jurisdiction, ContactInformation, OfficerID)
                                VALUES
                                (?, ?, ?, ?)
                                """,
                                (agency.agency_name, agency.jurisdiction, agency.contact_information, agency.officerID))
            self.connection.commit()
            print("Agency genrated✅")
            self.cursor.execute("""
                                SELECT TOP 1 *
                                FROM LawEnforcementAgency
                                ORDER BY AgencyID DESC;
                                """)
            agencies = self.cursor.fetchall()
            return agencies
        
        except Exception as e:
            print(e)

    def get_law_enforcement_agency_by_agency_id(self, agencyID):
        try:
            self.cursor.execute("""
                                select * 
                                from LawEnforcementAgency
                                where AgencyID = ? 
                                """,
                                (agencyID))
            agencies = self.cursor.fetchall()
            if len(agencies) == 0:
                raise LawEnforcementAgencyNumberNotFoundException
            else:
                return agencies
            
        except Exception as e:
            print("⚠️Oops error occured: ",e)

    def get_all_law_enforcement_agencies(self):
        try:
            self.cursor.execute("""
                                select * 
                                from LawEnforcementAgency
                                """)
            agency = self.cursor.fetchall()
            return agency
        
        except Exception as e:
            print(e)

    # Officer Management
    def create_officer(self, officer):
        try:
            self.cursor.execute("""
                                INSERT INTO Officers (FirstName, LastName, BadgeNumber, Rank, ContactInformation, AgencyID)
                                VALUES
                                (?, ?, ?, ?, ?, ?)
                                """,
                                (officer.firstname, officer.lastname, officer.badge_number, officer.rank, officer.contact_information, officer.agency_id))
            self.connection.commit()
            self.cursor.execute("""
                                SELECT TOP 1 *
                                FROM Officers
                                ORDER BY OfficerID DESC;
                                """)
            officers = self.cursor.fetchall()
            return officers
        
        except Exception as e:
            print(e)
            
    def get_officer_by_officer_id(self, officerID):
        try:
            self.cursor.execute("""
                                select * 
                                from Officers
                                where OfficerID = ? 
                                """,
                                (officerID))
            officer = self.cursor.fetchall()
            if len(officer) == 0:
                raise OfficerNumberNotFoundException
            else:
                return officer
            
        except Exception as e:
            print("⚠️Oops error occured: ",e)
    
    def get_all_officers(self):
        try:
            self.cursor.execute("""
                                select * 
                                from Officers 
                                """)
            officers = self.cursor.fetchall()
            return officers
        
        except Exception as e:
            print(e)


    # Suspect Managemnent
    def create_suspect(self, suspect):
        try:
            self.cursor.execute("""
                                INSERT INTO Suspects (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
                                VALUES 
                                (?, ?, ?, ?, ?)
                                """,
                                (suspect.firstname, suspect.lastname, suspect.date_of_birth, suspect.gender, suspect.contact_information))
            self.connection.commit()
            self.cursor.execute("""
                                SELECT TOP 1 *
                                FROM Suspects
                                ORDER BY SuspectID DESC;
                                """)
            suspects = self.cursor.fetchall()
            return suspects
        
        except Exception as e:
            print(e)

    def get_suspect_by_id(self, suspectID):
        try:
            self.cursor.execute("""
                                select * 
                                from Suspects
                                where SuspectID = ? 
                                """,
                                (suspectID))
            suspect = self.cursor.fetchall()
            if len(suspect) == 0:
                raise SuspectNumberNotFoundException
            else:
                return suspect
            
        except Exception as e:
            print("⚠️Oops error occured: ",e)

    def get_all_suspects(self):
        try:
            self.cursor.execute("""
                                select *
                                from Suspects
                                """)
            suspects = self.cursor.fetchall()
            return suspects
        
        except Exception as e:
            print(e)

    # Victim Managemnent
    def create_victim(self, victim):
        try:
            self.cursor.execute("""
                                INSERT INTO Victims (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
                                VALUES 
                                (?, ?, ?, ?, ?)
                                """,
                                (victim.firstname, victim.lastname, victim.date_of_birth, victim.gender, victim.contact_information))
            self.connection.commit()
            self.cursor.execute("""
                                SELECT TOP 1 *
                                FROM Victims
                                ORDER BY VictimID DESC;
                                """)
            victims = self.cursor.fetchall()
            return victims
        
        except Exception as e:
            print(e)

    def get_victim_by_id(self, victimID):
        try:
            self.cursor.execute("""
                                select * 
                                from Victims
                                where VictimID = ? 
                                """,
                                (victimID))
            victim = self.cursor.fetchall()
            if len(victim) == 0:
                raise VictimNumberNotFoundException
            else:
                return victim
            
        except Exception as e:
            print("⚠️Oops error occured: ",e)

    def get_all_victims(self):
        try:
            self.cursor.execute("""
                                select *
                                from Victims
                                """)
            victims = self.cursor.fetchall()
            return victims
        except Exception as e:
            print(e)