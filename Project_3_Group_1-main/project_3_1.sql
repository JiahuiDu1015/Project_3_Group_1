--Databases - Project_3_1

CREATE TABLE Job_ID (
	job_id INT PRIMARY KEY NOT NULL,
	job_field VARCHAR,
	job_location VARCHAR
);

-- CONSTRUCTION_SCRAPES

CREATE TABLE Data_Analyst_Scrapes (
	job_id INT,
	job_title VARCHAR,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

-- ENGINEERING_SCRAPES

CREATE TABLE Data_Engineer_Scrapes (
	job_id INT,
	job_title VARCHAR,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

CREATE TABLE Data_Analyst_Word_Count (
	word VARCHAR(255) not NULL UNIQUE,
	count INT
);

CREATE TABLE Data_Engineer_Word_Count (
	word VARCHAR (255) not NULL UNIQUE,
	count INT
);

-- Create tables for LOCATION COUNT

CREATE TABLE Allfields_Location_Count (
    job_location VARCHAR(255) NOT NULL UNIQUE,
    count INT DEFAULT 0
);


SELECT * FROM Allfields_Location_Count;