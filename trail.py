from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import base
import schema
import uvicorn
app=FastAPI()
class bool1(BaseModel):
    f: int
    p: int
@app.get('/')
def a():
    return {"sdf" :"fsdds"}

@app.get('/about/{id}')
def r(id : int):
    return {"df": id}

@app.post('/about/post/')
def r(id : int ,boo:base.bool1):
    return {"dfgdf":f"sds{boo.f}"}

