from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tarea = Column(String(150))

    def __repr__(self):
        return '<User %r>' % (self.id)
