import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

print("Program Starting")

# Load data
data = pd.read_csv(r'C:\Users\andre\Downloads\engineering_salaries.csv')

# Convert DataFrame to a 2D NumPy array
matrix = data.to_numpy()

# Extract unique colleges from the first column
colleges = sorted(list(set(matrix[:, 0].astype(str))))

def get_colleges(keyword):
    """Returns a list of colleges containing the keyword."""
    keyword = keyword.lower().strip()
    new_colleges = []
    seen = set()
    for college in colleges:
        college_str = str(college).lower()
        if keyword in college_str and college not in seen:
            new_colleges.append(college)
            seen.add(college)
    return sorted(new_colleges)

def get_majors_for_college(college):
    """Returns a list of engineering majors for the given college."""
    matching_rows = data[data['University'] == college]
    majors = sorted(list(set(matching_rows['Engineering Major'].astype(str))))
    return majors

def get_salary_data(college, major):
    """Returns 1-year and 5-year salaries for the given college and major."""
    row = data[(data['University'] == college) & (data['Engineering Major'] == major)]
    if not row.empty:
        salary_1yr = row['Median 1-Year Salary'].iloc[0]
        salary_5yr = row['Median 5-Year Salary'].iloc[0]
        return salary_1yr, salary_5yr
    return None, None

def predict_lifetime_earnings(salary_1yr, salary_5yr, years=40):
    """Predicts annual salaries over a career, returning years and salaries."""
    if salary_1yr is None or salary_5yr is None:
        return [], []
    years_range = np.arange(0, years + 1)
    salaries = []
    for year in years_range:
        if year <= 1:
            salary = salary_1yr
        elif year <= 5:
            salary = salary_1yr + (salary_5yr - salary_1yr) * (year - 1) / 4
        else:
            years_after_5 = year - 5
            salary = salary_5yr * (1 + 0.03) ** years_after_5
        salaries.append(salary)
    return years_range, salaries

# Create the main window
window = tk.Tk()
window.title("Project Four")
window.geometry("1000x1000")  # Enlarged window size
window.resizable(True, True)
window.minsize(600, 600)  # Minimum size
window.configure(bg="#f0f0f0")

# Center the window on the computer screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 1000
window_height = 1000
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a container frame
container = tk.Frame(window, bg="#f0f0f0")
container.pack(fill="both", expand=True)

# Create frames for screens
screen1 = tk.Frame(container, bg="#add8e6")
screen1.place(relwidth=1, relheight=1)
screen2 = tk.Frame(container, bg="#90ee90")
screen2.place(relwidth=1, relheight=1)
screen3 = tk.Frame(container, bg="#ffe4b5")
screen3.place(relwidth=1, relheight=1)

# --- Screen 1: College Dropdown ---
selected_college = tk.StringVar(window)
selected_college.set("Select College")

def show_selection(*args):
    """Update label and switch to screen2 if a valid college is selected."""
    selected = selected_college.get()
    label.config(text=f"Selected: {selected}")
    if selected not in ["Select College", "No matches"]:
        update_majors_dropdown(selected)
        screen2.tkraise()

selected_college.trace("w", show_selection)

label = tk.Label(screen1, text="Selected: None", bg="#add8e6", fg="#000080", font=("Arial", 16))
label.pack(pady=20)

screen1_label2 = tk.Label(screen1, text="Enter college keyword:", font=("Helvetica", 20))
screen1_label2.pack(pady=20)

entry = tk.Entry(screen1, bg="#ffffff", fg="#000000", insertbackground="#000000", width=50, font=("Arial", 12))
entry.pack(pady=20)

def update_dropdown():
    keyword = entry.get()
    new_colleges = get_colleges(keyword) if keyword else colleges
    dropdown["menu"].delete(0, "end")
    selected_college.set("Select College" if new_colleges else "No matches")
    for college in new_colleges:
        dropdown["menu"].add_command(
            label=college,
            command=lambda c=college: [selected_college.set(c), update_majors_dropdown(c), screen2.tkraise()]
        )
    if not new_colleges:
        label.config(text="Selected: No matches")

search_button = tk.Button(screen1, text="Search Colleges", command=update_dropdown,
                         bg="#4682b4", fg="white", activebackground="#5f9ea0", font=("Arial", 14))
search_button.pack(pady=20)

dropdown = tk.OptionMenu(screen1, selected_college, *colleges)
dropdown.config(bg="#ffffff", fg="#000000", activebackground="#87ceeb", activeforeground="#000000", width=50, font=("Arial", 12))
dropdown.pack(pady=20)

switch_button1 = tk.Button(screen1, text="Go to Screen 2", command=lambda: screen2.tkraise(),
                          bg="#4682b4", fg="white", activebackground="#5f9ea0", font=("Arial", 14))
switch_button1.pack(pady=20)

# --- Screen 2: Major Dropdown ---
selected_major = tk.StringVar(window)
selected_major.set("Select Major")

def show_major_selection(*args):
    """Update label and switch to screen3 if a valid major is selected."""
    selected = selected_major.get()
    major_label.config(text=f"Selected Major: {selected}")
    if selected not in ["Select Major", "No majors available"]:
        update_salary_display(selected_college.get(), selected)
        screen3.tkraise()

selected_major.trace("w", show_major_selection)

screen2_label = tk.Label(screen2, text="Select an Engineering Major:", bg="#90ee90", fg="#006400", font=("Arial", 20))
screen2_label.pack(pady=20)

major_label = tk.Label(screen2, text="Selected Major: None", bg="#90ee90", fg="#006400", font=("Arial", 16))
major_label.pack(pady=20)

major_dropdown = tk.OptionMenu(screen2, selected_major, "Select Major")
major_dropdown.config(bg="#ffffff", fg="#000000", activebackground="#98fb98", activeforeground="#000000", width=50, font=("Arial", 12))
major_dropdown.pack(pady=20)

def update_majors_dropdown(college):
    """Update the majors dropdown based on the selected college."""
    majors = get_majors_for_college(college) if college in colleges else []
    major_dropdown["menu"].delete(0, "end")
    selected_major.set("Select Major" if majors else "No majors available")
    for major in majors:
        major_dropdown["menu"].add_command(
            label=major,
            command=lambda m=major: [selected_major.set(m), update_salary_display(college, m), screen3.tkraise()]
        )
    major_label.config(text="Selected Major: None" if majors else "Selected Major: No majors available")

entry2 = tk.Entry(screen2, bg="#ffffff", fg="#000000", insertbackground="#000000", width=50, font=("Arial", 12))
entry2.pack(pady=20)
entry2.insert(0, "Type something...")

switch_button2 = tk.Button(screen2, text="Go to Screen 1", command=lambda: screen1.tkraise(),
                          bg="#3cb371", fg="white", activebackground="#66cdaa", font=("Arial", 14))
switch_button2.pack(pady=20)

# --- Screen 3: Salary and Earnings Plot ---
salary_label = tk.Label(screen3, text="Salary Information:", bg="#ffe4b5", fg="#8b4513", font=("Arial", 20))
salary_label.pack(pady=20)

salary_info = tk.Label(screen3, text="Select a major to see salary data", bg="#ffe4b5", fg="#8b4513", font=("Arial", 16))
salary_info.pack(pady=20)

# Plot with larger size
fig, ax = plt.subplots(figsize=(7, 5))
canvas = FigureCanvasTkAgg(fig, master=screen3)
canvas.get_tk_widget().pack(pady=20)

def update_salary_display(college, major):
    """Update salary labels and plot predicted lifetime earnings."""
    salary_1yr, salary_5yr = get_salary_data(college, major)
    if salary_1yr is not None and salary_5yr is not None:
        salary_text = f"1-Year Salary: ${salary_1yr:,.0f}\n5-Year Salary: ${salary_5yr:,.0f}"
        salary_info.config(text=salary_text)
    else:
        salary_info.config(text="Salary data not available")

    ax.clear()
    years, salaries = predict_lifetime_earnings(salary_1yr, salary_5yr)
    if years.size > 0:
        ax.plot(years, salaries, 'b-', label='Predicted Annual Salary')
        ax.set_xlabel('Years After Graduation', fontsize=14)
        ax.set_ylabel('Salary ($)', fontsize=14)
        ax.set_title(f'Lifetime Earnings for {major}\nat {college}', fontsize=16)
        ax.grid(True)
        ax.legend()
    else:
        ax.text(0.5, 0.5, 'No data to plot', horizontalalignment='center', verticalalignment='center', fontsize=14)
        ax.set_xlabel('Years After Graduation', fontsize=14)
        ax.set_ylabel('Salary ($)', fontsize=14)
    canvas.draw()

switch_button3 = tk.Button(screen3, text="Go to Screen 2", command=lambda: screen2.tkraise(),
                          bg="#cd853f", fg="white", activebackground="#deb887", font=("Arial", 14))
switch_button3.pack(pady=20)

# Initially show Screen 1
screen1.tkraise()

# Start the main event loop
window.mainloop()