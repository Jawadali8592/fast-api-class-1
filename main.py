from fastapi import FastAPI
from typing import List
import uvicorn
from typing import List


app=FastAPI()



students = [
    {'id': 1, 'name': 'Alice', 'age': 20, 'gender': 'Female'},
    {'id': 2, 'name': 'Bob', 'age': 21, 'gender': 'Male'},
    {'id': 3, 'name': 'Charlie', 'age': 19, 'gender': 'Male'},
    {'id': 4, 'name': 'Diana', 'age': 22, 'gender': 'Female'},
    {'id': 5, 'name': 'Eva', 'age': 20, 'gender': 'Female'}
]

@app.get("/students")
async def get_students():
    return students

@app.get("/students/{student_id}")
async def specific_student(student_id: int):
    for student in students:
        if student['id'] == student_id:
            return student
    return {'error': 'Student not found'}


























# @app.post('/jawad')
# def jawad():
#     num1  = 2
#     return('hello world')

# @app.get('/todo')
# def todo():
#     return('this is a todo app')

# @app.post("/path/{username}/{rollno}")
# def path1(username: str, rollno: str):
#     print(username, rollno)
#     return username + rollno

# @app.put('/card')
# def queryParams(username:str,rollno:str):
#     print(username.capitalize,rollno.capitalize)
#     return ('my name is ')





def start():
    uvicorn.run("class1.main:app",host="127.0.0.1",port=8080,reload=True)


    # studentslist:[]=[
    #     student(id=1,name="jawad",age=20,gender="male"),
    #     student(id=2,name="ALI",age=18,gender="male"),
    #     student(id=3,name="fatima",age=14,gender="female"),
    #     student(id=4,name="kashaf",age=23,gender="female"),
    #     student(id=5,name="ahmed",age=15,gender="male"),
    #     student(id=6,name="zehan",age=29,gender="male"),
    #     student(id=1,name="hassan",age=18,gender="male"),
        
    # ]