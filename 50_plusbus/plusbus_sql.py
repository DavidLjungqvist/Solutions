from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

from plusbus_data import Customer, Base

Database = 'sqlite:///plusbus.db'


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Customer(surname="Name1", contact_info="name1@mailadress.com"))
        new_items.append(Customer(surname="Name2", contact_info="name2@mailadress.com"))
        new_items.append(Customer(surname="Name3", contact_info="name3@mailadress.com"))
        new_items.append(Customer(surname="Name4", contact_info="name4@mailadress.com"))
        new_items.append(Customer(surname="Name5", contact_info="name5@mailadress.com"))
        session.add_all(new_items)
        session.commit()

if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)