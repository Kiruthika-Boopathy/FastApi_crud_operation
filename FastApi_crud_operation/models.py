from sqlalchemy import Column, Integer, String
from database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author = Column(String(255))
    description = Column(String(255))
    rating = Column(Integer)
