# Engineering Salary Trajectory Visualizer

This is a Tkinter-based GUI application that predicts and visualizes lifetime salary trajectories for engineering graduates based on their selected university and major. It uses an Excel-based dataset to generate a dynamic salary projection over a 40-year career span and presents the data in a line plot using Matplotlib.

## Features

- Dynamic college search using keyword input
- Dropdown selection of engineering majors specific to the chosen college
- Salary visualization using 1-year and 5-year median salaries
- Career earnings projection using an exponential growth model (3% annual increase after year 5)
- Interactive, multi-screen GUI built with Tkinter

## Dataset

The application uses a CSV file that includes the following columns:

- University
- Engineering Major
- Median 1-Year Salary
- Median 5-Year Salary

Make sure the dataset is named `engineering_salaries.csv` and is located at the correct path (modify the path in the script if necessary).

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries:

 
pip install pandas numpy matplotlib
Run the Python file:


python main.py
Usage
Start the application.

Enter a keyword to search for a college.

Select a college from the dropdown menu.

Choose an engineering major offered by that college.

View a graph of the predicted salary over a 40-year career.

The salary trajectory is calculated using the following logic:

Years 0–1: Constant at 1-year median salary

Years 2–5: Linear growth from 1-year to 5-year median salary

Years 6–40: Compounded annual 3% growth from 5-year salary

Notes
GUI supports window resizing and includes three screens for step-by-step input and output. 

To use a different dataset or add more columns (e.g., 10-year salary), update the CSV and modify the corresponding functions.

License
This project is released under the MIT License.

Let me know if you'd like to include instructions for bundling this into a `.exe` or `.app`, or if you wan
