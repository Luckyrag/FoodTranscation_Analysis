# FoodTranscation_Analysis
This project Provides the Analysis of the Food Allowance in 2 months using the Dataset from Govt. Free Source Data.
Overview
The "Food Distribution Analysis" project aims to analyze and visualize the food distribution data for two months, July and August, to gain insights into district-wise and day-wise transactions. This data-driven project uses Python and the Streamlit framework to create an interactive web application for stakeholders to explore the distribution trends and identify patterns that can help optimize future food distribution.

#### Key Features

Interactive User Interface:
A visually appealing home page with a central logo and title.
Sidebar navigation to switch between Introduction and Analysis sections.


Data Loading & Merging:
Utilizes the glob library to dynamically load and read all Excel files in July and August folders.
Merges data from both months using the pandas library for seamless comparison.
Data formatting and column reorganization ensure consistency and usability.


Introduction Section:
Overview:
Presents a summarized view of the day-wise total cards issued and availed for July and August.
Allows users to view individual district-wise transaction data for both months.


Details:
Includes descriptive statistics for the datasets, providing insights like mean, median, and other statistical summaries.


Analysis Section:

Data Visualization:
Bar and line charts visualize day-wise total availed cards for both months.
Interactive buttons to display various charts, including sorted transactions for easier interpretation.


Grouped Data Insights:
Leverages groupby operations to aggregate day-wise statistics for both months, enabling users to see trends at a glance.

##### Tools and Technology :
numpy , pandas , seaborn ,streamlit ,Matplotlib
