-- Dummy data for Victims table
INSERT INTO Victims (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
VALUES 
    ('John', 'Doe', '1985-05-15', 'Male', '1234 Elm St, (555) 123-4567'),
    ('Jane', 'Smith', '1990-07-22', 'Female', '5678 Oak St, (555) 234-5678'),
    ('Alice', 'Johnson', '1978-11-03', 'Female', '9101 Pine St, (555) 345-6789'),
    ('Bob', 'Brown', '1982-03-18', 'Male', '1213 Maple St, (555) 456-7890'),
    ('Charlie', 'Davis', '1995-09-09', 'Male', '1415 Birch St, (555) 567-8901'),
	('Diana', 'Clark', '1988-11-05', 'Female', '3344 Cedar Drive, 555-3344'),
	('Edward', 'Garcia', '1978-04-18', 'Male', '4455 Spruce Street, 555-4455'),
	('Fiona', 'Martinez', '1992-09-08', 'Female', '5566 Willow Way, 555-5566'),
	('George', 'Lopez', '1980-02-14', 'Male', '6677 Cherry Blvd, 555-6677'),
	('Hannah', 'Wilson', '1993-08-12', 'Female', '7788 Walnut Road, 555-7788');

-- Dummy data for Suspects table
INSERT INTO Suspects (FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES
('Michael', 'Adams', '1980-05-10', 'Male', '789 Elm Street, 555-1235'),
('Sarah', 'Baker', '1985-09-15', 'Female', '456 Oak Avenue, 555-6789'),
('David', 'Clark', '1970-03-22', 'Male', '321 Maple Drive, 555-9876'),
('Emily', 'Davis', '1992-07-12', 'Female', '654 Pine Road, 555-5432'),
('James', 'Evans', '1988-11-05', 'Male', '987 Birch Lane, 555-8765'),
('Jessica', 'Foster', '1995-02-18', 'Female', '123 Cedar Drive, 555-3456'),
('Robert', 'Garcia', '1976-12-25', 'Male', '789 Spruce Street, 555-6781'),
('Laura', 'Hernandez', '1982-08-30', 'Female', '456 Willow Way, 555-9012'),
('John', 'King', '1990-04-11', 'Male', '321 Cherry Blvd, 555-2345'),
('Anna', 'Lee', '1985-06-21', 'Female', '654 Walnut Road, 555-5678');

-- Dummy data for Incidents table
INSERT INTO Incidents (IncidentType, IncidentDate, Location_Latitude, Location_Longitude, Description, Status, VictimID, SuspectID) VALUES
('Robbery', '2024-05-01', 40.712800, -74.006000, 'Robbery at a convenience store', 'Open', 1, 1),
('Homicide', '2024-05-05', 34.052200, -18.243700, 'Homicide in downtown', 'Closed', 2, 2),
('Theft', '2024-05-10', 51.507400, -0.127800, 'Theft of jewelry from a store', 'Under Investigation', 3, 3),
('Robbery', '2024-05-15', 41.878100, -87.629800, 'Bank robbery', 'Open', 4, 4),
('Homicide', '2024-05-20', 33.749000, -84.388000, 'Homicide in a residential area', 'Open', 5, 5),
('Robbery', '2024-05-25', 29.760400, -95.369800, 'Robbery at a gas station', 'Closed', 6, 6),
('Theft', '2024-05-30', 34.052200, -18.243700, 'Theft of electronic devices', 'Open', 7, 7),
('Homicide', '2024-06-02', 40.712800, -74.006000, 'Homicide in a park', 'Open', 8, 8),
('Robbery', '2024-06-07', 34.052200, -18.243700, 'Robbery at a jewelry store', 'Closed', 9, 9),
('Theft', '2024-06-12', 41.878100, -87.629800, 'Theft of a vehicle', 'Open', 10, 10);

-- Dummy data for LawEnforcementAgency table
INSERT INTO LawEnforcementAgency (AgencyName, Jurisdiction, ContactInformation, Officer)
VALUES
('City Police Department', 'Citywide', '123 Police Ave, Cityville, USA', 'Officer Smith'),
('County Sheriff Office', 'Countywide', '456 Sheriff St, Countytown, USA', 'Sheriff Johnson'),
('State Bureau of Investigation', 'Statewide', '789 SBI Blvd, Capital City, USA', 'Agent Anderson'),
('Federal Bureau of Investigation', 'National', '321 FBI Lane, Washington DC, USA', 'Agent Brown'),
('Drug Enforcement Administration', 'National', '654 DEA Road, Washington DC, USA', 'Agent Davis'),
('Immigration and Customs Enforcement', 'National', '987 ICE Drive, Washington DC, USA', 'Agent Miller'),
('Transportation Security Administration', 'National', '741 TSA Parkway, Washington DC, USA', 'Agent Wilson'),
('Secret Service', 'National', '852 Secret Way, Washington DC, USA', 'Agent Taylor'),
('Bureau of Firearms and Explosives', 'National', '369 ATF Street, Washington DC, USA', 'Agent Martinez'),
('United States Marshals Service', 'National', '159 Marshals Lane, Washington DC, USA', 'Marshal Garcia');

INSERT INTO Officers (FirstName, LastName, BadgeNumber, Rank, ContactInformation, AgencyID)
VALUES
('John', 'Smith', 12345, 'Police Officer', '123 Police Ave, Cityville, USA', 1),
('Lisa', 'Johnson', 23456, 'Deputy Sheriff', '456 Sheriff St, Countytown, USA', 2),
('Mark', 'Anderson', 34567, 'Special Agent', '789 SBI Blvd, Capital City, USA', 3),
('Jennifer', 'Brown', 45678, 'Special Agent', '321 FBI Lane, Washington DC, USA', 4),
('William', 'Davis', 56789, 'Special Agent', '654 DEA Road, Washington DC, USA', 5),
('Michelle', 'Miller', 67890, 'Special Agent', '987 ICE Drive, Washington DC, USA', 6),
('James', 'Wilson', 78901, 'Special Agent', '741 TSA Parkway, Washington DC, USA', 7),
('Stephanie', 'Taylor', 89012, 'Special Agent', '852 Secret Way, Washington DC, USA', 8),
('John', 'Martinez', 90123, 'Special Agent', '369 ATF Street, Washington DC, USA', 9),
('Emily', 'Garcia', 01234, 'Deputy Marshal', '159 Marshals Lane, Washington DC, USA', 10);

-- Dummy data for Evidence table
INSERT INTO Evidence (Description, LocationFound, IncidentID)
VALUES
('Weapon - handgun', 'Near store counter', 1),
('Blood samples', 'Alley floor', 2),
('Surveillance footage', 'Department store cameras', 3),
('Security camera footage', 'Bar security system', 4),
('Fingerprints', 'Window sill', 5),
('Witness testimony', 'Park visitors', 6),
('Gasoline canister', 'Abandoned building', 7),
('Financial records', 'Bank statements', 8),
('Spray paint cans', 'Near vandalized property', 9),
('Drugs - cocaine', 'Underground hideout', 10);

INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status)
VALUES
(1, 1, '2024-04-02', 'Initial incident report filed', 'Draft'),
(2, 2, '2024-04-06', 'Crime scene investigation report', 'Finalized'),
(3, 3, '2024-04-11', 'Suspect apprehension report', 'Finalized'),
(4, 4, '2024-04-16', 'Witness interviews report', 'Draft'),
(5, 5, '2024-04-21', 'Evidence collection report', 'Finalized'),
(6, 6, '2024-04-26', 'Child recovery report', 'Finalized'),
(7, 7, '2024-05-01', 'Arson investigation report', 'Draft'),
(8, 8, '2024-05-06', 'Financial fraud report', 'Finalized'),
(9, 9, '2024-05-11', 'Vandalism incident report', 'Draft'),
(10, 10, '2024-05-16', 'Drug trafficking bust report', 'Finalized');

select * from Incidents;
select * from Victims;
select * from Suspects;
select * from LawEnforcementAgency;
select * from Officers;
select * from Evidence;
select * from Reports;












