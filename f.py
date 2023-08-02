from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app=FastAPI()
class Student(BaseModel):
    name:str
    age:int
    year:int

@app.get('/')
def index():
    return {'name':'First Data'}
students={
    1:
    {"name":"john","age":17,"class":"year 12"}
}
class UpdateStudent(BaseModel):
    name :Optional[str]
    age: Optional[int]
    year:Optional[int]


@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get_student")
def get_student(name:str):
    for student_id in students:
        if(students[student_id]["name"]=='john'):
            return students[student_id]
    return {"sdfjsdf"}

@app.post("/create_student/{student_id}")
def create_student(student_id :int,student:Student):
    if(student_id in students):
        return {"Error:Student exists"}

    students[student_id]=student
    return students[student_id]

@app.put("/update_student/{student_id}")
def update_student(student_id : int, student: UpdateStudent):
    if(student_id not in students):
        return {"Error: Student does not exist"}
    #if student.name!= None
    students[student_id]=student
    return students[student_id]

@app.delete("/delte_Student/{student_id}")
def delete(student_id:int):
    if( student_id not in students):
        return{'Eroor':'ods'}
    
    del students[student_id]
    return {"sfs":"sfdsdf"}