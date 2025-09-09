import os
import shutil

base_path = "C:/Python/Python_Bootcamp/Classes_Objects"
filePath = os.path.join(base_path, "students.txt")
new_file_path = os.path.join(base_path, "student_records.txt")
school_dir = os.path.join(base_path, "SchoolData")
moved_file_path = os.path.join(school_dir, "student_records.txt")

def WriteStudent():
    try:
        with open(filePath,"w") as f:   
            n = int(input("Enter the numbers of students to be added"))

            for i in range(1, n+1):
                print("Enter details for students: ")
                name = input("Enter name of the student : ")
                roll = int(input("Enter roll number of student "))
                marks = int(input("Enter marks of student "))
                f.write(f"{name},{roll},{marks}\n")

        print("Data Saved Successfully ")
    except Exception as e:
        print("An Error Occured")


def ReadStudents():
    try:
        
        with open(filePath, "r") as f:
            print("Student Records:\n")
            for line in f:
                line = line.strip()
                print(line)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)



def RenameFilePathName():
    try:
        os.rename(filePath, new_file_path)
        print(f"File renamed successfully to {new_file_path}")
    except FileNotFoundError:
        print("The file does not exist.")
    except FileExistsError:
        print("A file with the new name already exists.")
    except Exception as e:
        print("An error occurred:", e)

def DirectoryOperations():
    try:
        if not os.path.exists(school_dir):
            os.mkdir(school_dir)
            print(f"Directory created: {school_dir}")
        else:
            print(f"Directory already exists: {school_dir}")

        shutil.move(new_file_path, moved_file_path)
        print(f"File moved to {moved_file_path}")

        print("\nfiles inside SchoolData:")
        for file in os.listdir(school_dir):
            print(file)

    except FileNotFoundError:
        print("student_records.txt not found")
    except Exception as e:
        print("an error occurred ", e)


def DeleteOperations():
    try:
        if os.path.exists(moved_file_path):
            os.remove(moved_file_path)
            print("student_records.txt deleted.")
        else:
            print("File not found inside SchoolData.")

        if os.path.exists(school_dir):
            os.rmdir(school_dir)
            print("SchoolData directory deleted.")
        else:
            print("⚠️ SchoolData directory does not exist.")

    except Exception as e:
        print("An error occurred during delete operation:", e)


#Menu--------------------------------------------------

while True:
    print("1. Write Student Records")
    print("2. Read Student Records")
    print("3. Rename File")
    print("4. Directory Operations")
    print("5. Delete Operations")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        WriteStudent()
    elif choice == "2":
        ReadStudents()
    elif choice == "3":
        RenameFilePathName()
    elif choice == "4":
        DirectoryOperations()
    elif choice == "5":
        DeleteOperations()
    elif choice == "6":
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please choose between 1 to 6.")
