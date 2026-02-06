from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.models.Survey import StudentSurvey
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/submit-survey")
def submit_survey(data: dict, db: Session = Depends(get_db)):
    try:
        new_entry = StudentSurvey(**data)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return {"message": "Survey saved successfully!"}
    except Exception as e:
        return {"message": f"Error saving to database: {str(e)}"}