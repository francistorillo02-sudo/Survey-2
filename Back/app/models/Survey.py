from sqlalchemy import Column, Integer, String, Text
from app.database import Base 

class StudentSurvey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)
    year = Column(String)
    gender = Column(String)
    rating = Column(Integer)
    email = Column(String)
    comments = Column(Text)