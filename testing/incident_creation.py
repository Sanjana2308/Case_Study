import unittest

from dao.crime_analysis import CrimeAnalysisServiceImpl

from entity.incidents import Incidents

from myexception.exception import IncidentNumberNotFoundException

class TestCrimeAnalysisServiceImpl(unittest.TestCase):
    def setUp(self):
        self.service = CrimeAnalysisServiceImpl()
        self.test_incident = Incidents("Initial incidence", "2024-04-23", 23.65, 23.66, "Stolen", "Open", "23", "23")
        self.test_incident_id = self.service.create_incident(self.test_incident)

        self.assertIsNotNone(self.test_incident_id)

    def test_create_incident(self):
        incident_type = "Robbery"
        incident_date = '2024-08-23'
        location_longitude = 24.6
        location_latitude = 52.36
        description = "Stolen"
        status = "Open"
        victim_id = 2
        suspect_id = 2

if __name__ == "__main__":
    unittest.main()