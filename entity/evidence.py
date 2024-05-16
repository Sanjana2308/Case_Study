class Evidence:
    def init(self, description: str, location_found: str, incident_id: int):
        self.description = description
        self.location_found = location_found
        self.incident_id = incident_id

    # Getter methods
    def get_description(self):
        return self.description

    def get_location_found(self):
        return self.location_found

    def get_incident_id(self):
        return self.incident_id

    # Setter methods
    def set_description(self, description: str):
        self.description = description

    def set_location_found(self, location_found: str):
        self.location_found = location_found

    def set_incident_id(self, incident_id: int):
        self.incident_id = incident_id