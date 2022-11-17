from sqlalchemy import Column, Integer, REAL, TEXT, MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db_data.sqlite")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Elements(Base):
    """
    Прописываем класс таблицы.
    Важно, наименования и типы полей должны соответствовать наименованиям в базе.
    Поэтому тут пришлось назвать на русском, что неправильно
    Иначе работать не будет
    """
    __tablename__ = 'data_forces'

    rowid = Column(Integer, primary_key=True)
    Элемент = Column(Integer)
    Сеч = Column(Integer)
    Вид = Column(Integer)
    sX = Column(REAL)
    sY = Column(REAL)
    txy = Column(REAL)
    mx = Column(REAL)
    my = Column(REAL)
    mz = Column(REAL)
    mk = Column(REAL)
    mxy = Column(REAL)
    n = Column(REAL)
    qx = Column(REAL)
    qy = Column(REAL)
    qz = Column(REAL)
    rz = Column(REAL)
    Тип = Column(TEXT)
    Формула = Column(TEXT)


if __name__ == '__main__':
    meta = MetaData()
    Base = declarative_base()

    engine = create_engine("sqlite:///db_data.sqlite")  # указываем драйвер и относительный путь, у меня лежит прям в папке с файлом
    meta.create_all(engine)

    session = Session(bind=engine)

    # достаем одно значение какое-то
    all_elements = session.query(Elements).filter(Elements.sX == "89.539").all()

    for obj in all_elements:
        print(f'Элемент: {obj.Элемент}, Какие-то значения, например txy: {obj.txy}')

    # достаем where sX>90
    sX_for_filter = 89
    all_elements_2 = session.query(Elements).filter(Elements.sX > sX_for_filter).all()
    for obj in all_elements_2:
        print(f'Элемент: {obj.Элемент}, Какие-то значения, где sX>{sX_for_filter}: например txy: {obj.txy}, sX: {obj.sX}')

    # считаем количество элементов где например sX > 89
    count_elements = session.query(Elements).filter(Elements.sX > 89).count()
    print(f'Значений где sX> 89: ', count_elements)


    # примеры фильтров https://pythonru.com/biblioteki/crud-sqlalchemy-orm