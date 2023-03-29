"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

sqlite_database = "sqlite:///Books.db"
engine = create_engine(sqlite_database)

class Base (DeclarativeBase): pass
class Reader(Base):
    __tablename__ = "reader"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = relationship("Book", back_populates="reader")

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String)
    reader_id = Column (Integer, ForeignKey("reader.id")) 
    reader = relationship("Reader", back_populates="books")

Base.metadata.create_all(bind=engine) 


with Session(autoflush=False, bind=engine) as db:
    reader1 = Reader(name = 'Игнат')
    reader2 = Reader(name = 'Косяковка')
    reader3 = Reader(name = 'Виталька')
    book1 = Book(name = 'Белые розы<3', author = 'Марк Твен')
    book2 = Book(name = 'Кукакреку', author = 'Марк II')
    book3 = Book(name = 'Инстафамка', author = 'Марк Гутентак')
    book4 = Book(name = 'Маленький Принц', author = 'Экзюпери')
    reader1.books = [book1]
    reader2.books = [book4]
    reader3.books = [book3]
    reader1.books.append(book2)
    db.add_all([reader1, reader2, reader3])
    db.commit()



with Session(autoflush=False, bind=engine) as db:
    # получение всех объектов
    readers = db.query(Reader).all() 
    for r in readers:
        print(r.name)
        for i in  r.books:
            print('    ', i.name, ' - ', i.author)


