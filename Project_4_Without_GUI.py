
"""
===============================================================================
ENGR 130 Spring 2024 - Project 4


    I am creating a program that will calculate an engineer's median lifetime earnings.
    It will analyze data calculated from numerous sources such as College Scorecard, Glassdoor, etc.,
    to provide the user with their college and median salary. I selected this theme, since it allows
    engineers or engineering graduates to gauge their earnings over a career to make better guided financial decisions.
     Many graduates have no idea about their major's predicted earnings, and lose valuable money paying off student debt,
      purchasing unnecessary items, and overspending on living expenses. I want to make their earnings clear so that they
      don't run into these mistakes.


    Assignment:     Project 4
    Author:         Andrew Becker, becke198@purdue.edu

    Citations
    I found the try-except and .tolist() methods online on W3 schools.
    Used Chat-GPT to generate the file data from many online sources including glassdoor and college scorecard.

===============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Project_4_SecondFunction

print("Program Starting")

# Load data (for grading purposes, file is engineering_salaries.csv)
data = pd.read_csv(r'engineering_salaries.csv')

# Convert DataFrame to a 2D NumPy array
matrix = data.to_numpy()

#Creates the colleges
colleges = matrix[:,0].tolist()
majors = matrix[:, 1].tolist()
sals_1 = matrix[:, 2].tolist()
sals_5 = matrix[:, 3].tolist()


def get_colleges(keyword):
    """Returns the colleges for what is entered in the search bar"""
    keyword = keyword.lower().strip()
    new_colleges = []
    seen = []
    for college in colleges:
        college_str = str(college).lower()
        if keyword in college_str and college not in seen:
            new_colleges.append(college)
            seen.append(college)
    if new_colleges == []:
        for college in colleges:
            if college not in seen:
                new_colleges.append(college)
                seen.append(college)
        return sorted(new_colleges)
    return sorted(new_colleges)

def get_majors_for_college(college):
    """Returns a list of engineering majors for the given college."""
    matching_rows = data[data['University'] == college]
    majors_list = []
    for index in range(len(colleges)):
        if colleges[index] == college:
            majors_list.append(majors[index])

    #majors = sorted(list(set(matching_rows['Engineering Major'].astype(str))))
    return majors_list

def get_salary_data(college, major):
    """Returns 1-year and 5-year salaries for the given college and major."""
    for index in range(len(colleges)):
        if colleges[index] == college and majors[index] == major:
            try:
                sal_1 = float(sals_1[index])
                sal_5 = float(sals_5[index])
                return sal_1, sal_5
            except:
                return None, None
    return None, None
    #Error checking algorithm 1 returns None if salary info is not found from file




def main():

    #Get college input
    college = ""
    college = input("Enter college (or keyword): ")
    while college not in colleges:

        print(f"College not found. Available colleges:")
        for c in get_colleges(college):
            print(c)
        college = input("Enter college (or keyword): ")

    #get major input
    major = ""
    print(f"Available majors:")
    for m in get_majors_for_college(college):
        print(m)
    major = input("Enter major: ")


    #error checking algorithm
    while major not in get_majors_for_college(college):
        print(f"Error: Major not found.\n Available majors:")
        for m in get_majors_for_college(college):
            print(m)

        major = input("Enter major: ")

    sal_1,sal_5 = get_salary_data(college, major)


    x,y = Project_4_SecondFunction.predict_lifetime_earnings(sal_1, sal_5)

    #prints the output to console
    if len(x) == 0 and len(y) == 0:
        print(f"\n\nError: Data is not available")
    else:
        #makes sure the program does not crash. If it does, an error message is displayed.
        try:
            print(f" The median salary 1 year after graduation for a {major} major at {college} is ${int(sal_1):,}")
            print(f" The median salary 5 years after graduation for a {major} major at {college} is ${int(sal_5):,}")

            #plot starts
            plt.plot(x,y)
            plt.xlabel("Time (Years)")
            plt.ylabel("Salary ($)")
            plt.title("Plot of Salary ($) per Year")
            plt.show()
        except:
            print(f"\n\nError: Data is not available")




if __name__ == "__main__":
    main()