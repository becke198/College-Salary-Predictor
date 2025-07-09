# Engineering Salary Trajectory Visualizer

A Tkinter-based GUI application that predicts and visualizes lifetime salary trajectories for engineering graduates, based on selected universities and majors. It reads data from a CSV file and plots a 40-year salary projection using Matplotlib.

---

## 📌 Features

-  **Dynamic college search** via keyword input  
-  **Major selection** tailored to the chosen college  
-  **Salary visualization** using median 1-year and 5-year salaries  
-  **Career earnings projection** using:
  - Constant salary (Years 0–1)
  - Linear growth (Years 2–5)
  - 3% annual exponential growth (Years 6–40)  
- 🖥 **Multi-screen interactive GUI** built with Tkinter  
-  **Responsive layout** with support for window resizing  

---

## 📂 Dataset

The application uses a CSV file named `engineering_salaries.csv`, which should contain the following columns:

- `University`
- `Engineering Major`
- `Median 1-Year Salary`
- `Median 5-Year Salary`

Ensure the CSV is placed in the correct directory (adjust the file path in the script if needed).

---

## 🛠 Requirements

- Python 3.x  
- `pandas`  
- `numpy`  
- `matplotlib`  

Install dependencies with:

```bash
pip install pandas numpy matplotlib
🚀 How to Run
Clone or download this repository.

Open a terminal and navigate to the project directory.

Run the main script:

bash
Copy
Edit
python main.py
💡 Usage Instructions
Launch the application.

Enter a keyword to search for a university.

Select a university from the dropdown.

Choose an engineering major offered at that university.

View a graph of projected salary over a 40-year career.

 ### Salary Projection Logic
Years 0–1: Salary remains constant at the 1-year median

Years 2–5: Salary increases linearly from 1-year to 5-year median

Years 6–40: Salary grows 3% annually, compounded from the 5-year value

 ### Notes
- The GUI is fully resizable and follows a multi-screen layout for a step-by-step experience.

- You can adapt the application for a different dataset (e.g., including 10-year salaries) by updating the CSV file and modifying the relevant logic in the code.



### License
This project is licensed under the MIT License.
