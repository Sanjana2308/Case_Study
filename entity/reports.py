class Reports:
    def __init__(self, incident_id: int, reporting_officer: int, report_date, report_details, status):
        self.__incident_id = incident_id
        self.__reporting_officer = reporting_officer
        self.__report_date = report_date
        self.__report_details = report_details
        self.__status = status