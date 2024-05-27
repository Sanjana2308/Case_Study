from util.DBConnection import DBConnection

from .crime_analysis_interface import IcrimeAnalysisService

from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims

from myexception.exception import IncidentNumberNotFoundException, CaseNumberNotFoundException, ReportNumberNotFoundException

class CrimeAnalysisServiceImpl(DBConnection, IcrimeAnalysisService): 

    def create_incident(self, incidents):
        
        try:
            self.cursor.execute("""INSERT INTO Incidents(IncidentType, IncidentDate, Location_Longitude, Location_Latitude, Description, Status, VictimID, SuspectID) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                                    (incidents.incident_type, incidents.incident_date, incidents.location_latitude, incidents.location_longitude, incidents.description, incidents.status, incidents.victim_id, incidents.suspect_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)

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
            print("Oops error happened!!",e)

    def generate_incident_report(self, report):
        try:
            self.cursor.execute(
                """
                INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status)
                VALUES (?, ?, ?, ?, ?)
                """,
                (report.incident_id, report.reporting_officer, report.report_date, report.report_details, report.status)
                )
            print("Report Generated")
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

            if len(reports == 0):
                raise ReportNumberNotFoundException
            else:
                return reports

        except Exception as e:
            print("Oops error happened: ",e)

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
            print("Oops error happened: ",e)
    
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
          
    

    


