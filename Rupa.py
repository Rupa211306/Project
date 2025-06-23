import matplotlib.pyplot as plt

def compute_total_marks(data):
    for student in data:
        student['Total Marks'] = student['CT(20)'] + student['Final(72)'] + student['Att(8)']

def compute_grade_point(marks):
    if marks >= 80:
        return 4.0
    elif marks >= 70:
        return 3.5
    elif marks >= 60:
        return 3.0
    elif marks >= 50:
        return 2.5
    elif marks >= 40:
        return 2.0
    else:
        return 0.0

def add_grade_points(data):
    for student in data:
        student['Grade Point'] = compute_grade_point(student['Total Marks'])

def save_to_csv(data, filename='GP.csv'):
    with open(filename, 'w') as file:
        file.write("Roll no,Name,Total Marks,Grade Point\n")
        for student in data:
            file.write(f"{student['Roll no']},{student['Name']},{student['Total Marks']},{student['Grade Point']}\n")

def print_student_data(data):
    print("Roll no | Name           |Total Marks      |Grade Point")
    print("--------------------------------------------------")
    for student in data:
        print(f"{student['Roll no']:7} | {student['Name']:13} | {student['Total Marks']:11} | {student['Grade Point']:.1f}")

def plot_total_marks_distribution(data):
    roll_nos = [student['Roll no'] for student in data]
    total_marks = [student['Total Marks'] for student in data]
    plt.scatter(roll_nos, total_marks, color='blue', alpha=0.5)
    plt.xlabel('Student Roll No')
    plt.ylabel('Total Marks')
    plt.title('Total Marks Distribution')
    plt.xticks(rotation=90)
    plt.grid()
    plt.show()

data = [
    {'Roll no': 192201, 'Name': 'Mohamed', 'CT(20)': 15, 'Final(72)': 60, 'Att(8)': 6},
    {'Roll no': 192202, 'Name': 'Youssef', 'CT(20)': 8, 'Final(72)': 62, 'Att(8)': 0},
    {'Roll no': 192204, 'Name': 'Ahmed', 'CT(20)': 17, 'Final(72)': 45, 'Att(8)': 8},
    {'Roll no': 192205, 'Name': 'Mahmoud', 'CT(20)': 13, 'Final(72)': 10, 'Att(8)': 1},
    {'Roll no': 192206, 'Name': 'Mustafa', 'CT(20)': 19, 'Final(72)': 32, 'Att(8)': 8},
    {'Roll no': 192208, 'Name': 'Yassin', 'CT(20)': 10, 'Final(72)': 51, 'Att(8)': 0},
    {'Roll no': 192210, 'Name': 'Taha', 'CT(20)': 18, 'Final(72)': 32, 'Att(8)': 7},
    {'Roll no': 192211, 'Name': 'Khaled', 'CT(20)': 13, 'Final(72)': 25, 'Att(8)': 2},
    {'Roll no': 192212, 'Name': 'Hamza', 'CT(20)': 13, 'Final(72)': 18, 'Att(8)': 3},
    {'Roll no': 192213, 'Name': 'Bilal', 'CT(20)': 12, 'Final(72)': 57, 'Att(8)': 3},
    {'Roll no': 192214, 'Name': 'Ibrahim', 'CT(20)': 18, 'Final(72)': 46, 'Att(8)': 8},
    {'Roll no': 192215, 'Name': 'Hassan', 'CT(20)': 17, 'Final(72)': 38, 'Att(8)': 6},
    {'Roll no': 192216, 'Name': 'Hussein', 'CT(20)': 13, 'Final(72)': 28, 'Att(8)': 3},
    {'Roll no': 192217, 'Name': 'Karim', 'CT(20)': 17, 'Final(72)': 34, 'Att(8)': 6},
    {'Roll no': 192218, 'Name': 'Tareq', 'CT(20)': 17, 'Final(72)': 60, 'Att(8)': 8},
    {'Roll no': 192220, 'Name': 'Abdel-Rahman', 'CT(20)': 16, 'Final(72)': 48, 'Att(8)': 7},
    {'Roll no': 192221, 'Name': 'Ali', 'CT(20)': 14, 'Final(72)': 5, 'Att(8)': 5},
    {'Roll no': 192222, 'Name': 'Omar', 'CT(20)': 18, 'Final(72)': 37, 'Att(8)': 8},
    {'Roll no': 192223, 'Name': 'Halim', 'CT(20)': 15, 'Final(72)': 56, 'Att(8)': 4},
    {'Roll no': 192224, 'Name': 'Murad', 'CT(20)': 19, 'Final(72)': 43, 'Att(8)': 8},
    {'Roll no': 182204, 'Name': 'Selim', 'CT(20)': 12, 'Final(72)': 33, 'Att(8)': 0},
    {'Roll no': 182215, 'Name': 'Abdallah', 'CT(20)': 18, 'Final(72)': 59, 'Att(8)': 8}
]

compute_total_marks(data)
add_grade_points(data)
save_to_csv(data)
print_student_data(data)
plot_total_marks_distribution(data)