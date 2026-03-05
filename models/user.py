from sqlalchemy import Column, String, Integer, Identity, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Identity(always=False), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)

    def to_dict(self):

        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }
