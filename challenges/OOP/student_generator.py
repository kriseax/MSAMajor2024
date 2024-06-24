import Student

def load_students(file_name):
    list_of_students = []

    
    #create a file handler
    file = open(file_name, "r")

    #create variable to keep track of line in file that we are reading
    line_number = 0
    #read file line by line in for loop
    for line_of_data in file:
        line_number += 1
        #skip first line in csv file
        if line_number == 1:
            continue
        
        #split the line of data at the comma
        student_data = line_of_data.split(",")

        #handle errors in data format. line_of_data should have 6 items
        #if error in format then write a message to a log file and continue reading from the file
        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as err:
            print(str(err))
            continue

        #get student data and create a student object for each student
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            student_id = student_data[5].strip()
        except:
            print(f"Error: {err} on line {line_number}")
            continue

        new_student = Student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
        list_of_students.append(new_student)
    
    
    return list_of_students


def main():
    #Create 2 instances of Student
    list_of_students = load_students("students.csv")

    for student in list_of_students:
        student.print_student_data()

main()