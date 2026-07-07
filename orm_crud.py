from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "postgresql://postgres:29101216@localhost:5432/user_management"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(id={self.id}, title='{self.title}')"
    
Base.metadata.create_all(engine)

new_user = User(
    name="Velu",
    email="velu@gmail.com"
)

session.add(new_user)
session.commit()

print("User added!")

new_post = Post(
    title="Education",
    content="I completed my Bachelors in Information Technology",
    user_id=new_user.id
)

session.add(new_post)
session.commit()

print("Post added!")