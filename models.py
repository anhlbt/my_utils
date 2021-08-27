# coding: utf-8

# sqlacodegen mysql+mysqldb://root:lbtanh@localhost/fabm_db > backend/models.py
# python ./expose_existing/expose_existing.py mysql+mysqldb://root:lbtanh@localhost/fabm_db --host 0.0.0.0 --port 5555


from sqlalchemy import Column, DateTime, ForeignKey, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'categories'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    sort = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(INTEGER(11), server_default=text("'1'"))


class Member(Base):
    __tablename__ = 'members'

    id = Column(INTEGER(11), primary_key=True)
    nick_name = Column(String(255), nullable=False)
    real_name = Column(String(255), nullable=False)
    sex = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    birth_date = Column(DateTime, nullable=False)
    phone = Column(String(255), nullable=False)
    openid = Column(String(255), nullable=False)
    status = Column(INTEGER(11), server_default=text("'1'"))


class Order(Base):
    __tablename__ = 'orders'

    id = Column(INTEGER(11), primary_key=True)
    order_number = Column(String(255), nullable=False)
    repast_date = Column(String(255))
    repast_time = Column(String(255))
    seat_no = Column(INTEGER(11))
    remark = Column(String(255))
    status = Column(INTEGER(11), server_default=text("'1'"))


class Person(Base):
    __tablename__ = 'people'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    sort = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(INTEGER(11), server_default=text("'1'"))


class Seat(Base):
    __tablename__ = 'seats'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    sort = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(INTEGER(11), server_default=text("'1'"))


class Time(Base):
    __tablename__ = 'times'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    sort = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(INTEGER(11), server_default=text("'1'"))


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(INTEGER(11), server_default=text("'1'"))


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
    url = Column(String(255))
    desc = Column(Text)
    sort = Column(INTEGER(11), server_default=text("'0'"))
    cid = Column(ForeignKey('categories.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    status = Column(INTEGER(11), server_default=text("'1'"))

    category = relationship('Category')


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(INTEGER(11), primary_key=True)
    mid = Column(INTEGER(11))
    did = Column(ForeignKey('dishes.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    num = Column(INTEGER(11))
    status = Column(INTEGER(11), server_default=text("'1'"))

    dish = relationship('Dish')


class OrderDish(Base):
    __tablename__ = 'order_dishes'

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(ForeignKey('orders.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    dishes_id = Column(ForeignKey('dishes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    dishes_num = Column(INTEGER(11), nullable=False)
    dishes_price = Column(String(255), nullable=False)
    status = Column(INTEGER(11), server_default=text("'1'"))

    dishes = relationship('Dish')
    order = relationship('Order')
