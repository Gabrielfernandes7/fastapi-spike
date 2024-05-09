from sqlalchemy import Column, Integer, String
from database.connnection import Base, engine

# Não instancio novamente o Base = declarative_base()
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(20))

    def __init__(self, username):
        self.username = username

Base.metadata.create_all(bind = engine)
