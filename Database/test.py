
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# строка подключения
sqlite_database = "sqlite:///persons.db"

# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)

# создаем базовый класс для моделей www
class Base (DeclarativeBase): pass

# создаем модель, объекты которой будут храниться в бд
class Person(Base):

    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer, )

# создаем таблицы
Base.metadata.create_all(bind=engine) 

with Session(autoflush=False, bind=engine) as db:
    #создаем объект Person для добавления в бд
    tom = Person(name="Tom", age=38)
    db.add(tom) # добавляем в бд
    db.commit() # сохраняем изменения или db.refresh()

people = db.query(Person).filter(Person.name == 'Tom').all()


with Session(autoflush=False, bind=engine) as db: # получаем один объект, у которого id=1 
    tom = db.query(Person).filter(Person.id==1).first()
    if (tom != None):
        print(f"{tom.id}.{tom.name} ({tom.age})") 
        # 1.Tom (38)

        # изменениям значения
        tom.name = "Tomas"
        tom.age = 22

        db.commit() # соxраняем изменения

# with Session(autoflush=False, bind=engine) as db:
#     bob = db.query(Person).filter(Person.id==2).first()
#     db.delete(bob) # удаляем обьект 
#     db.commit() # сохраняем изменения

