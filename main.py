from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Student Management API")


class Student(BaseModel):
    id: int
    name: str
    department: str
    semester: int
    cgpa: float


# Temporary database
students = []


# GET all students
@app.get("/students")
def get_students():
    return students


# GET single student
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# POST create student
@app.post("/students")
def create_student(student: Student):

    # Check duplicate ID
    for existing_student in students:
        if existing_student["id"] == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student.model_dump())

    return {
        "message": "Student created successfully",
        "student": student
    }


# PUT update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for index, item in enumerate(students):

        if item["id"] == student_id:

            students[index] = student.model_dump()

            return {
                "message": "Student updated successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DELETE student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )