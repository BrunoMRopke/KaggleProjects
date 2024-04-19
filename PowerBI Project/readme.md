# Introduction
This project serves as a practical simulation of data analysis expectations and outcomes within a professional environment, grounded in personal study and experience in the field of data analysis. The dataset analyzed, which is 67MB in size and sourced from the Kaggle platform, was chosen to deepen understanding of the Power BI platform's capabilities. All analyses conducted as part of this project were purely for educational purposes, aiming to replicate the kind of insights and challenges one might encounter in a real-world data analysis scenario.

# Step-by-Step Guide

##  Step 1: Sourcing the Data
###  Obtaing the dataset from Kaggle.
The data used in this dashboard is sourced from Kaggle, a well-known platform in the fields of analysis and data science. Kaggle is extensively used by professionals for accessing free datasets and for sharing solutions and insights in data science.
Data Source used in this project: https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data

## Step 2: Preprocessing Data with Google Cloud Storage and Google BigQuery
Google Cloud Storage and Google BigQuery were chosen for their robustness and capability to handle large datasets efficiently. These platforms not only ensure high performance and scalability but also offer seamless integration that facilitates smooth data workflows, greatly minimizing complexities in data transfer. Particularly, Google BigQuery stands out by allowing the creation of new views, enabling precise data manipulation and selection of specific datasets needed for analysis. This feature is crucial for tailoring data processing to meet exact analytical requirements, enhancing the overall efficiency and effectiveness of our data operations. This strategic choice supports our goal to maintain a scalable, high-performance, and streamlined data environment to meet and exceed stakeholder expectations.
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/61d527a5-b640-4971-b031-71be0567da77)


## Step 3: Utilizing Google Cloud Storage and Google BigQuery
Objective: Ensure the dataset is ready for analysis and alleviate resources when executing queries in the tool.
Action: Within Google Colab, utilize Python and SQL commands to perform initial formatting of the dataset and generate dimension tables. This process involves:
Analyzing the dataset to identify potential dimension tables.
Using Python for data manipulation tasks, such as filtering, cleaning, and structuring data.
Employing SQL queries to further refine and create dimension tables, which will be used in Power BI for more efficient querying.
The alternation between Python and SQL commands serves not only to optimize the data for analysis but also as an educational exercise to understand different approaches to data manipulation and preparation.
### SQL Query Views
This BigQuery SQL query is executed to enhance the sales data with geographic information, making it more informative and useful for analysis in Power BI. The step ensures that when the data is imported into Power BI, it already includes matched city names, district names, and state names by postal code, which facilitates a more nuanced geographic analysis and reporting within the dashboard. The use of a view allows for dynamic and efficient data retrieval, providing up-to-date geographic matching without the need for data replication or additional storage. The approach taken here aligns with best practices for data management by offloading data processing to BigQuery, leveraging its powerful infrastructure to handle complex queries, which improves the performance and responsiveness of the Power BI dashboard.
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/15e35b7b-3007-4154-a3a4-d096ffce2fc2)

### Python Queries
Google BigQuery's integration with Python Notebooks stands as a robust feature, enabling data analysts and scientists to perform complex data manipulations and apply machine learning models directly within the database environment. This capability allows for the execution of advanced analytical computations and machine learning processes on large datasets before they are loaded into visualization tools like Power BI, Looker, and others.

## Step 4: Loading the Data into Power BI Using QuickQuery or Direct Import
With the views prepared and optimized in Google Big Query, the datasets were directly imported into Power BI Desktop. This approach was chosen because it does not impact the data update routines or compromise access security. Direct import ensures that the dashboard developed in Power BI remains both dynamic and secure, supporting interactive visualization and in-depth analysis of the data without disrupting ongoing data management practices.
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/976fc54f-37a6-4e5c-97b9-502fb3e26b85)

## Step 5: Data Preparation and Cleaning
Objective: Optimize and clean the data for analysis.
Action: After loading the data into Power BI, apply Power Query Editor to perform data preparation and cleaning tasks. This includes:
Removing unnecessary columns to streamline the dataset.
Handling missing values either by removing rows, replacing with suitable values, or imputing based on data patterns.
Transforming data types for accurate analysis (e.g., converting string dates to datetime format).
Creating calculated columns if necessary to enhance the data model for more in-depth analysis.
These steps are crucial for ensuring the data is in the best possible shape for creating meaningful visualizations and extracting reliable insights.

## Step 6: Developing the Relational Model and Creating Visualizations  
Objective: Develop visual representations of your data and construct a relational model to uncover insights.
Action:
Developing the Relational Model: Before diving into visualization, focus on defining the relational entities among the tables. This involves establishing clear relationships between your main dataset and the dimension tables, including the ones created in previous steps. Utilize Power BI's data modeling tools to accurately represent these relationships, ensuring a robust foundation for analysis.

### Creating a Date Reference Table:
Recognizing the importance of date-based analysis in this project, create a dedicated Date table. This table is generated based on the historical date range present within the dataset and is designed to support future calculations, such as time-based trends and comparative analysis over different periods. The Date table becomes a central piece in the relational model, linking to other tables where date fields are relevant.
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/5a34be12-efa8-4f8c-bc47-173d5f773880)


Visualization: With the relational model set, including the Date table, proceed to utilize Power BI’s visualization tools. Create charts, graphs, and tables that highlight the data’s patterns, trends, and anomalies. The established relational model allows for dynamic and complex analyses, facilitated by the comprehensive Date table. Experiment with different visualization types to best convey the story behind the data, taking advantage of the relational model to explore various angles and depths of analysis.
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/bf4283f5-a5c5-4054-b722-278d3ca1bbba)
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/f0383cef-b9af-4f96-a52f-75949b876659)
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/9b7eb8f6-56bb-4fbb-a6a5-d5ef2cd6fea1)
![image](https://github.com/BrunoMRopke/MyProjects/assets/38227297/83537075-a41e-493d-a0db-addfea05ef5b)

## Step 7: Analyzing the Data and Implementing Access Control
Implementing Access Control: After completing the visual representations and analysis, the next step involves securing the access to these insights. Utilize the workspace environment in Microsoft 365 to create specific roles that define access levels to the Power BI reports and dashboards. These roles can be tailored to match the organization’s hierarchy or project team structure, ensuring that sensitive information is only accessible to authorized users. Follow these sub-steps to implement access control:

Navigate to the workspace settings in your MS365 Power BI environment.
Select or create a new workspace dedicated to this project.
Within the workspace, go to the "Access" tab and start defining roles. These could be roles like "Admin," "Editor," and "Viewer," each with different permissions regarding the ability to edit, view, or manage the workspace and its content.
Assign users to these roles based on their need to access the data and the level of interaction they require with the reports and dashboards.
By controlling access through roles and workspace settings, you ensure that data insights are shared responsibly within the organization, aligning with data governance policies and protecting sensitive information.

Conclusion
By simulating the analytical expectations and outcomes of a professional environment, this project not only enhances understanding of the Power BI platform but also prepares one for the dynamic challenges and opportunities in the field of data analysis. The experience gained from analyzing real-world datasets, like the one from Kaggle, and translating these analyses into actionable insights, is invaluable for anyone looking to advance in the field of data science and analytics.
