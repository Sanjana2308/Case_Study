import unittest
from dao import CrimeAnalysisServiceImpl
from entity import Incidents

class TestIncidentServiceModule(unittest.TestCase):
    def setUp(self):
        self.crime_analysis_service = CrimeAnalysisServiceImpl()
        self.test_incident = Incidents("Robbery", '2024-05-03', 23.56, 32.56, "Stolen items", "Open", 2, 3)
        self.test_incident_id = self.crime_analysis_service.create_incident(self.test_incident)
        self.assertIsNotNone(self.test_incident_id)

    def test_create_incident(self):
        incident_type = "Theft"
        incident_date = "2024-05-09"
        location_longitude = 24.36
        location_latitude = 25.63
        description = "Stolen"
        status = "Closed"
        victim_id = 3
        suspect_id = 4
        new_incident = Incidents(incident_type, incident_date, location_longitude, location_latitude, description, status, victim_id, suspect_id)
        created_incident = self.crime_analysis_service.create_incident(new_incident)
        self.assertIsNotNone(created_incident)
        print("-"*20+"test_create_incident passed"+"-"*20)

    # def test_update_incident(self):
    #     updated_status = "Open"
    #     updated_incident = self.crime_analysis_service.update_incident_status(self.test_incident_id, updated_status)
        
    #     # Check after updating the movie
    #     self.crime_analysis_service.cursor.execute(
    #         """select * 
    #         from Incidents 
    #         where IncidentID = ?
    #         """,(self.test_incident_id,)
    #         )
    #     incident = self.crime_analysis_service.cursor.fetchone()
        


        

if __name__ == "__main__":
    unittest.main()