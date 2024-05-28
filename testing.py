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

        print("\n\n"+"🎊 "*5+"test_create_incident passed!"+"🎊 "*5)
        
    def test_update_incident(self):
        updated_status = "Open"
        incident_num = [x for x in self.test_incident_id]
        updated_incident = self.crime_analysis_service.update_incident_status(incident_num[0], updated_status)

        # Check after updating the incident
        self.crime_analysis_service.cursor.execute(
            """select * 
            from Incidents 
            where IncidentID = ?
            """,(incident_num[0])
            )
        incident = self.crime_analysis_service.cursor.fetchone()
        self.assertEqual(incident[6], "Open")
        
        print("\n\n"+"🎊 "*5+"test_update_incident passed!"+"🎊 "*5)

if __name__ == "__main__":
    unittest.main()