CREATE DATABASE Project2;
USE Project2;

CREATE TABLE Victims(
	VictimID INT PRIMARY KEY IDENTITY(1, 1),
	FirstName VARCHAR(255) NOT NULL,
	LastName VARCHAR(255) NOT NULL,
	DateOfBirth DATE NOT NULL,
	Gender VARCHAR(50),
	ContactInformation VARCHAR(50)
);

CREATE TABLE Suspects(
	SuspectID INT PRIMARY KEY IDENTITY(1, 1),
	FirstName VARCHAR(50) NOT NULL,
	LastName VARCHAR(50) NOT NULL,
	DateOfBirth DATE NOT NULL,
	Gender VARCHAR(50),
	ContactInformation VARCHAR(255)
);

CREATE TABLE Incidents(
	IncidentID INT PRIMARY KEY IDENTITY(1, 1),
	IncidentType VARCHAR(255) NOT NULL,
	IncidentDate DATE NOT NULL,
	Location_Longitude DECIMAL(10, 8) NOT NULL,
	Location_Latitude DECIMAL(10, 8) NOT NULL,
	Description VARCHAR(200),
	Status VARCHAR(50) NOT NULL,
	VictimID INT,
	SuspectID INT
	FOREIGN KEY (VictimID) References Victims(VictimID),
	FOREIGN KEY (SuspectID) References Suspects(SuspectID)
);

CREATE TABLE LawEnforcementAgency(
	AgencyID INT PRIMARY KEY IDENTITY(1, 1),
	AgencyName VARCHAR(255) NOT NULL,
	Jurisdiction VARCHAR(255) NOT NULL,
	ContactInformation VARCHAR(200),
	Officer VARCHAR(30)
);

CREATE TABLE Officers(
	OfficerID INT PRIMARY KEY IDENTITY(1, 1),
	FirstName VARCHAR(255) NOT NULL,
	LastName VARCHAR(255) NOT NULL,
	BadgeNumber INT,
	Rank VARCHAR(50),
	ContactInformation VARCHAR(200),
	AgencyID INT
	FOREIGN KEY (AgencyID) References LawEnforcementAgency(AgencyID) 
);

CREATE TABLE Evidence(
	EvidenceID INT PRIMARY KEY IDENTITY(1,1), 
	Description VARCHAR(200) NOT NULL,
	LocationFound VARCHAR(50) NOT NULL,
	IncidentID INT
	FOREIGN KEY (IncidentID) References Incidents (IncidentID)
);

CREATE TABLE Reports(
	ReportID INT PRIMARY KEY IDENTITY(1, 1),
	IncidentID INT,
	ReportingOfficer INT,
	ReportDate DATE NOT NULL,
	ReportDetails VARCHAR(500),
	Status VARCHAR(20) NOT NULL,
	FOREIGN KEY (IncidentID) References Incidents (IncidentID),
	FOREIGN KEY (ReportingOfficer) References Officers (OfficerID)
);

CREATE TABLE Cases(
	CaseID INT PRIMARY KEY IDENTITY(1, 1),
	CaseDescription VARCHAR(500),
	IncidentID INT,
	FOREIGN KEY (IncidentId) References Incidents(IncidentId)
);