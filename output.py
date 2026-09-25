def list_stu(students):
    print("\n" + "=" * 60)
    print("\nThe list of all students is:")
    print("=" * 60)
    for i in students:
        print(f"ID: {i.get_stu_id()} | Name: {i.get_stu_name()} | DoB: {i.get_dob()}|GPA: {i.get_stu_gpa():.2f}")
def list_cou(courses):
    print("\n" + "=" * 60)
    print("\nThe list of all courses is:")
    print("=" * 60)
    for i in courses:
        print(f"Course ID: {i.get_cou_id()} | Course Name: {i.get_name()} | Credits: {i.get_credits()}")
def display_marks(cou,stu,marks):
    # __marks = {} 
    cou_id = input("\nThe course to be selected (ID): ")
    selected_course = next((c for c in cou if c.get_cou_id() == cou_id), None)
    course_name = selected_course.get_name() if selected_course else cou_id
    print(f"\n--- Marks for Course: {course_name} ({cou_id}) ---")
    if cou_id not in marks:
        marks[cou_id] = {}
    for stu in stu:
        mark = marks[cou_id].get(stu.get_stu_id())
        print(f"ID: {stu.get_stu_id()} | Name: {stu.get_stu_name()} | Mark: {mark}")