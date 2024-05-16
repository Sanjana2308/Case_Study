class Officers:
    def init(self, firstname, lastname, badge_number, rank, contact_information, agency_id: int):
        self.firstname = firstname
        self.lastname = lastname
        self.badge_number = badge_number
        self.rank = rank
        self.contact_information = contact_information
        self.agency_id = agency_id

     # Getter methods
    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_badge_number(self):
        return self.badge_number

    def get_rank(self):
        return self.rank

    def get_contact_information(self):
        return self.contact_information

    def get_agency_id(self):
        return self.agency_id

    # Setter methods
    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_badge_number(self, badge_number):
        self.badge_number = badge_number

    def set_rank(self, rank):
        self.rank = rank

    def set_contact_information(self, contact_information):
        self.contact_information = contact_information

    def set_agency_id(self, agency_id: int):
        self.agency_id = agency_id

