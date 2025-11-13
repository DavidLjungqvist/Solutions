from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer

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
