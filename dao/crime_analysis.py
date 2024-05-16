from util.DBConnection import DBConnection

# from .crime_analysis_interface import IcrimeAnalysisService

from entity import Evidence, Incidents, LawEnforcementAgency, Officers, Reports, Suspects, Victims

class CrimeAnalysisServiceImpl(DBConnection): #IcrimeAnalysisService

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
            for incident in incidents:
                print(incident)

        except Exception as e:
            print(e)


        
