from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Date
from sqlalchemy import String, Integer
from dateutil import parser

Base = declarative_base()


class Customer(Base):
    __tablename__ = "Kunder"
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    contact_info = Column(String)

    def convert_to_tuple(self):
        return self.id, self.surname, self.contact_info

    def valid(self):
        try:
            value = len(self.surname)
        except ValueError:
            return False
        return value > 0

    @staticmethod
    def convert_from_tuple(tuple_):
        customer = Customer(id=tuple_[0], surname=tuple_[1], contact_info=tuple_[2])
        return customer

class Travel(Base):
    __tablename__ = "Rejser"
    id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(Date)
    capacity = Column(Integer)

    def convert_to_tuple(self):
        return self.id, self.route, self.date, self.capacity

    def valid(self):
        try:
            value = len(self.route)
        except ValueError:
            return False
        return value > 0

    @staticmethod
    def convert_from_tuple(tuple_):
        date = parser.parse(tuple_[2])
        travel = Travel(id=tuple_[0], route=tuple_[1], date=date, capacity=tuple_[3])
        return travel

class Booking(Base):
    __tablename__ = "Bookinger"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer#, ForeignKey("customer.id"), nullable=False)
    )
    travel_id = Column(Integer#, ForeignKey("travel.id"), nullable=False)
    )
    reserved_seats = Column(Integer)

    def convert_to_tuple(self):
        return self.id, self.customer_id, self.travel_id, self.reserved_seats



    @staticmethod
    def convert_from_tuple(tuple_):
        booking = Booking(id=tuple_[0], customer_id=tuple_[1], travel_id=tuple_[2], reserved_seats=tuple_[3])
        return booking
