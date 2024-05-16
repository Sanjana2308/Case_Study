class Evidence:
    def __init__(self, description: str, location_found: str, incident_id: int):
        self.__description = description
        self.__location_found = location_found
        self.__incident_id = incident_id