#### Viewership-Analysis
This repository contains Python scripts analyzing TV viewership data across platforms, event types, and top videos.

#### Introduction
This dataset captures viewer interaction with video content across different platforms. It records when viewers watched, who they were, how long they engaged, the type of event that occurred during playback, and the specific video titles. Such data is crucial for analysing user engagement, viewing behaviour, and platform performance.

#### Overview
The analysis focuses on:
- **Total Watch Time by Platform** – Comparison of audience engagement across devices such as Mobile, TV, and Web.
- **Watch Time by Event Type** – Breakdown of viewing activity by play, pause, and other engagement events.
- **Top 5 Most-Watched Videos** – Identification of the most popular videos based on total viewing time.
- **The aim**of this dataset is to provide insights into customer viewing patterns and platform usage, enabling better understanding of user preferences and engagement levels.

#### Objectives: To
1. Analyze Total Watch Time across different platforms (e.g., Mobile, TV, Web) to understand where audiences engage most.
2. Examine Watch Time by Event Type to identify viewing behaviors such as plays, pauses, and completions.
3. Identify Top-Performing Videos based on total time watched to highlight high-performing content.

#### Data Description
The dataset includes the following columns:
- **DateID** – Date of the viewing event
- **CustomerID** – Unique identifier for each customer
- **TotalTimeWatched** – Duration of video watched (in seconds)
- **Platform** – Device or platform used for viewing
- **PlayEventType** – Type of play event (e.g., play, pause, stop)
- **VideoTitle** – Title of the video content

#### Visualizations
Explore the interactive graph pictures here 👇

###### Total Watch Time by Platform
![Platform Watch Time](https://dbc-17f06863-5d5b.cloud.databricks.com/editor/files/2039598156760314?o=120978430381930)
**Insight:** Leanback has the highest total watch time, followed by Web, Android, and iOS.

##### Total Watch Time by Event Type
![Event Type Watch Time](https://dbc-17f06863-5d5b.cloud.databricks.com/editor/files/2039598156760315?o=120978430381930)
**Insight:** Live TV dominates in watch time, followed by Catchup and Other, while Downloads show no watch time.

##### Top 5 Videos by Watch Time
![Top Videos](https://dbc-17f06863-5d5b.cloud.databricks.com/editor/files/2039598156760316?o=120978430381930)
**Insight:** Unknown' tops watch time, followed by South African Morning and South African Tonight, while The Block Australia and Suidooster have lower watch time among the top 5.

#### Tools & Templates to Use
Imported Library-Library is a collection of pre-written code that you can use to perform common tasks without having to write the code from scratch.They are built-in and are used by importing them with the import statement.
- **Pandas** Pandas are for data analysis, manupulation and  working with tables/excel sheets (DataFrames).
-(Import pandas as pd)
- **Nump** Numpy is for numerical operations or math functions.
-(Import numpy as np)
- **Matplotlib** to create viewership visualizations, 
-(Import matplotlib.pyplot as plt)
- **!pip install openpyxl**- Allows to open an Excel file and read data:
- **Excel sheet**: For initial data.
- **Python**: For Coding.

#### Summary
This dataset tracks customer video consumption by watch time, platform, and content. It reveals viewing trends, popular videos, and audience preferences to guide recommendations and engagement strategies.
