# Project_3_Group_1 
# Job Market Insights: A Web Scraper for Data Analyst and Data Engineer Job Ads

  # Project Proposal
The project objective is to assist job seekers in finding a job. Scraped data will be used to analyse the most popular requirements for certain fields to help job seekers identify which jobs they are qualified for, or necessary skills they may need to obtain.

Every employer uses different terms and words in job listings.


# Data sources: 
Seek: https://www.seek.com.au/jobs/in-All-Australia

(permmision: Confidential Information
Communications between you and the SEEK Group should be regarded as confidential unless we expressly provide otherwise. You may only use such confidential information for the purposes of performing your obligations or exercising your rights under these Terms. You must not disclose confidential information to any third party without our prior written consent. If you are unsure about whether any information that is communicated to you is confidential in nature, you should treat that information as confidential and confirm with us prior to disclosure of that information.(https://talent.seek.com.au/partners/terms-of-use/))

# The process
Once we had our data, we utilized a jupyter notebook to clean our data and export it as csv files to use in pgAdmin 4. 
The data was ready, we used pgAdmin 4 to create tables, populate the tables with the appropriate data, and then generate the queries needed for our data analysis. 
Below is the ERD graph. 

![Business process flow](https://github.com/user-attachments/assets/69b33047-18df-49a9-b878-719345c661de)


# Built With

  - Flask - The web framework used
      
  - Plotly.js - JavaScript library for creating interactive charts
  - HTML, CSS
  - Software: Visual Studio Code
  - Python
      - Beautiful Soup
      - requests
      - psycopg2 (not covered in course)
      - os (not covered in course)
  - SQL
      - pgAdmin 4
  - GitHub

# Conclusion
The Job Search Helper has successfully demonstrated its utility as a comprehensive tool for job seekers. By leveraging a structured approach to organizing and analyzing job data, the project provides valuable insights and streamlines the job search process.

Key Outcomes:
Efficient Data Management: The project effectively utilizes data structures like dictionaries and DataFrames to organize and manage job-related information. This structured approach ensures that data is easily accessible and analyzable.

Enhanced Data Filtering: By implementing filtering techniques, such as excluding words with fewer than four characters, the tool refines job search criteria, making it easier to focus on relevant and substantial job details.

Seamless Database Integration: The integration with PostgreSQL allows for efficient storage and retrieval of job data. The use of connection parameters and libraries like SQLAlchemy and psycopg2 facilitates smooth interactions with the database, ensuring that data management tasks are handled efficiently.

User-Friendly Insights: The project offers a clear view of job-related metrics and information, aiding users in making informed decisions. The ability to filter and analyze job data enhances the overall user experience by providing actionable insights.

Future Enhancements:
 - Advanced Analytics: Implementing more advanced analytics features, such as trend analysis and predictive modeling, could further enhance the tool’s capabilities and provide deeper insights into job market trends.
 - User Interface: Developing a user-friendly interface for the tool could make it more accessible to a broader audience, including those less familiar with programming and data analysis.
 - Integration with Job Boards: Connecting the tool with popular job boards and job search engines could automate data retrieval and improve the timeliness and relevance of job information.

Overall, The Job Search Helper has laid a strong foundation for a tool that simplifies and improves the job search experience. By continuing to build on its features and capabilities, the project holds the potential to become an indispensable resource for job seekers.

