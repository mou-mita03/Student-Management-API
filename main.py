from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    department: str
    semester: int
    cgpa: float


students = []


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id:int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404,
                        detail="Student not found")



@app.post("/students")
def create_student(student:Student):

    students.append(student.dict())

    return student



@app.put("/students/{student_id}")
def update_student(student_id:int, student:Student):

    for index,item in enumerate(students):

        if item["id"] == student_id:

            students[index]=student.dict()

            return student


    raise HTTPException(status_code=404,
                        detail="Student not found")



@app.delete("/students/{student_id}")
def delete_student(student_id:int):

    for student in students:

        if student["id"]==student_id:

            students.remove(student)

            return {
                "message":"Deleted successfully"
            }


    raise HTTPException(status_code=404,
                        detail="Student not found")