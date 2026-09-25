students = []
courses = []
marks = {}
def input_stu():
    cnt = int(input("The Number of Students: "))
    print("Please enter the information of the students:")
    for _ in range(cnt):
        stu_id = input("\tStudent's ID is: ")
        stu_name = input("\tStudent's Name is: ")
        dob = input("\tStudent's DOB is: ")
        students.append({"id": stu_id, "name": stu_name, "dob": dob})
def input_cou():
    cnt = int(input("The Number of Courses: "))
    print("Please enter the information of the Courses:")
    for _ in range(cnt):
        cou_id = input("\tCourse ID: ")
        cou_name = input("\tCourse Name: ")
        courses.append({"id": cou_id, "name": cou_name})
def input_marks():
    course_id = input("\nSelect a course ID: ")
    selected_course = next((c for c in courses if c["id"] == course_id), None)
    course_name = selected_course["name"] if selected_course else course_id
    print(f"Course name: {course_name}\n")
    if course_id not in marks:
        marks[course_id] = {}
    for stu in students:
        mark = float(input(f"\tEnter {stu['name']}'s mark: "))
        marks[course_id][stu["id"]] = mark
def list_stu():
    print("\nThe list of all students is:")
    for stu in students:
        print(f"ID: {stu['id']} | Name: {stu['name']} | DoB: {stu['dob']}")
def list_cou():
    print("\nThe list of all courses is:")
    for cou in courses:
        print(f"Course ID: {cou['id']} | Course Name: {cou['name']}")
def display_marks():
    course_id = input("\nThe course to be selected (ID): ")
    selected_course = next((c for c in courses if c["id"] == course_id), None)
    course_name = selected_course["name"] if selected_course else course_id
    print(f"\n--- Marks for Course: {course_name} ({course_id}) ---")
    for stu in students:
        mark = marks.get(course_id, {}).get(stu["id"], "N/A")
        print(f"ID: {stu['id']} | Name: {stu['name']} | Mark: {mark}")
list_stu()
input_cou()
list_cou()
print("\nPlease enter the marks of the course: ")
while True:
    input_marks()
    choice = input("\n another? (yes/no) *** ")
    if choice == "no":
        break
while True:
    display_marks()
    choice = input("\n another? (yes/no) *** ")
    if choice == "no":
        break