class Incidents:
    def __init__(self, incident_type, incident_date, location_longitude, location_latitude, description, status, victim_id, suspect_id):
        self.incident_type = incident_type
        self.incident_date = incident_date
        self.location_longitude = location_longitude
        self.location_latitude = location_latitude
        self.description = description
        self.status = status
        self.victim_id = victim_id
        self.suspect_id = suspect_id


    def set_incident_type(self, incident_type):
        self.incident_type = incident_type

    def set_incident_date(self, incident_date):
        self.incident_date = incident_date

    def set_location_longitude(self, location_longitude):
        self.location_longitude = location_longitude

    def set_location_latitude(self, location_latitude):
        self.location_latitude = location_latitude

    def set_description(self, description):
        self.description = description

    def set_status(self, status):
        self.status = status

    def set_victim_id(self, victim_id):
        self.victim_id = victim_id

    def set_suspect_id(self, suspect_id):
        self.suspect_id = suspect_id

     # Getter methods
    def get_incident_type(self):
        return self.incident_type

    def get_incident_date(self):
        return self.incident_date

    def get_location_longitude(self):
        return self.location_longitude

    def get_location_latitude(self):
        return self.location_latitude

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_victim_id(self):
        return self.victim_id

    def get_suspect_id(self):
        return self.suspect_id

    


    