class Reports:
    def init(self, incident_id: int, reporting_officer: int, report_date, report_details, status):
        self.incident_id = incident_id
        self.reporting_officer = reporting_officer
        self.report_date = report_date
        self.report_details = report_details
        self.status = status

    # Getter methods
    def get_incident_id(self):
        return self.incident_id

    def get_reporting_officer(self):
        return self.reporting_officer

    def get_report_date(self):
        return self.report_date

    def get_report_details(self):
        return self.report_details

    def get_status(self):
        return self.status

    # Setter methods
    def set_incident_id(self, incident_id: int):
        self.incident_id = incident_id

    def set_reporting_officer(self, reporting_officer: int):
        self.reporting_officer = reporting_officer

    def set_report_date(self, report_date):
        self.report_date = report_date

    def set_report_details(self, report_details):
        self.report_details = report_details

    def set_status(self, status):
        self.status = status
    