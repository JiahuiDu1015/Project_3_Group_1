--Databases - Project_3_1

-- Create tables for SCRAPED DATA
-- JOB_ID

CREATE TABLE Job_ID (
	job_id INT PRIMARY KEY NOT NULL,
	job_field VARCHAR,
	job_location VARCHAR
);

-- Data_Analyst_Scrapes

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

-- Data_Engineer_Scrapes

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

-- Create tables for WORD COUNT

-- Data_Analyst_Word_Count

CREATE TABLE Data_Analyst_Word_Count (
	word VARCHAR(255) not NULL UNIQUE,
	count INT
);

-- Data_Engineer_Word_Count

CREATE TABLE Data_Engineer_Word_Count (
	word VARCHAR (255) not NULL UNIQUE,
	count INT
);


SELECT * from data_engineer_word_count;