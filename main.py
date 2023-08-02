from fastapi import FastAPI,Depends
import models
import database
from database import engine,SessionLocal
import schemas
from sqlalchemy.orm import Session
app=FastAPI()

models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/about/post/')
def r(request:schemas.bool1,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    

