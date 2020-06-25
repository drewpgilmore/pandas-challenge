import pandas as pd
#name paths for reference files
schools_file = "Resources/schools_complete.csv"
students_file = "Resources/students_complete.csv"
school_data = pd.read_csv(schools_file)
student_data = pd.read_csv(students_file)
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

district_summary = pd.DataFrame({
    'Total Schools': [len(school_data_complete["school_name"].unique())],
    'Total Students': [school_data_complete["student_name"].count()],
    'Total Budet': [school_data_complete.budget.unique().sum()],
    'Average Math Score': [school_data_complete["math_score"].sum()/school_data_complete["math_score"].count()],
    'Average Reading Score': [school_data_complete["reading_score"].sum()/school_data_complete["reading_score"].count()],
    '% Passing Math': [school_data_complete["math_score"].sum()/school_data_complete["math_score"].count()],
    '% Passing Reading': [school_data_complete["math_score"].sum()/school_data_complete["math_score"].count()],
    '% Overall Passing': [school_data_complete["math_score"].sum()/school_data_complete["math_score"].count()],
})
district_summary.head()

school_summary = school_data_complete.groupby('school_name')
