"""
настройка базы данных фильмов состоящая из столбцов: идентификатор, название, год выпуска, жанр, рейтинг.
функция настройки для добавления фильма в базу, получения всех фильмов, просмотра фильма по универсальному циклу, обновления рейтинга, извлечения фильма.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///films1.sql"

engine = create_engine(sqlite_database)

class Base (DeclarativeBase): pass

class Films(Base):

    __tablename__ = "film"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(Integer, )
    janr = Column(String)
    rate = Column(Integer, )

Base.metadata.create_all(bind=engine) 

def create(f_name, f_date, f_janr, f_rate):
    with Session(autoflush=False, bind=engine) as db:
        #создаем объект Person для добавления в бд
        film = Films(name=f_name, date=f_date, janr = f_janr, rate = f_rate)
        db.add(film) # добавляем в бд
        db.commit() # сохраняем изменения или db.refresh()

def info_by_name(name_film):
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).filter(Films.name == name_film).all()
        for i in films:
            print(i.name)

def info():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).all()
        for i in films:
            print(i.name)


def change_by_id(id_ch, name, date, janr, rate):
    with Session(autoflush=False, bind=engine) as db: # получаем один объект, у которого id=1 
        film = db.query(Films).filter(Films.id==id_ch).first()
        if (film != None):
            # print(f"{film.id}.{film.name} ({film.date}), {film.janr}, {film.rate}") 
            film.name = name
            film.date = date
            film.janr = janr
            film.rate = rate
            db.commit()

def delete(id_del):
    with Session(autoflush=False, bind=engine) as db:
        dele = db.query(Films).filter(Films.id==id_del).first()
        db.delete(dele) # удаляем обьект 
        db.commit() # сохраняем изменения

create("Tom and Jerry", 1956, 'Комедия', 5)
create("Пираты карибского моря", 2006, 'Комедия, Приключения', 10)
create("Игнат", 2004, 'Комедия', 1)
info()
info_by_name('Игнат')
change_by_id(3, "Игнат не крут", 2005, 'Комедия', 2)
info_by_name('Игнат')
info()
delete(3)
info()