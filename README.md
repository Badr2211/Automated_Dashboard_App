
# Automated and Interactive Dashboard for Data Analytics

## Introduction
Welcome to our Automated and Interactive Dashboard project! This tool is designed to assist data analysts in creating intuitive dashboards and to help stakeholders with no analytical background understand their data with ease. Our dashboard includes a built-in Gemini model that analyzes graphs and presents insights in an understandable format.

by defult data set (Churn Dataset) 😍 
you can try

## Features
- **Automated Dashboard Creation**: Generate dashboards quickly with minimal input.

- **Interactive User Interface**: Engage with your data through a user-friendly interface.

- **Gemini Model Integration**: Leverage our AI model to analyze and interpret complex data.

- **No Expertise Required**: Designed for users without a technical background.


  

## Installation

To run this app, you need to have Python 3 and Streamlit installed on your system. 


You can install Streamlit with the following command:

first thing you must open .envy file and assign your Google_API_KEy

```
cd src
```

```bash
pip install -r requirements.txt
```
Then, clone this repository to your local machine, and navigate to the project folder. To launch the app, run the following command:

```
streamlit run streamlit.py 
```
This will open the app in your default browser.

# Usage

The app has a simple and intuitive interface. On the left sidebar, you can upload your dataset by dragging and dropping or browsing files. The app supports CSV and Excel files, with a limit of 200 MB per file. After uploading your dataset, you can select the target column for specific insights. The app will display basic information and statistics about your dataset, such as number of rows, columns, missing values, data types, etc. You can also explore the data with interactive dashboards, such as histograms, box plots, scatter plots, etc. You can customize the visualizations by selecting the features, colors, and sizes

you can click button analysis plot to ask Gemini model analysis the plot 


# Contributing

This project is open for contributions. If you find any bugs or have any suggestions, please feel free to open an issue or submit a pull request.



