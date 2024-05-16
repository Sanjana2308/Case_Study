class Incidents:
    def __init__(self, incident_type: str, incident_date, location_longitude, location_latitude, description, status, victim_id: int, suspect_id: int):
        self.__incident_type = incident_type
        self.__incident_date = incident_date
        self.__location_longitude = location_longitude
        self.__location_latitude = location_latitude
        self.__description = description
        self.__status = status
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id
