from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

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

def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam)) # list of objects??
        result = []
        for record in records:
            result.append(record)
    return result

def create_record(record):
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()

def update_customer(customer):
    with Session(engine) as session:
        session.execute(update(Customer).where(Customer.id == customer.id).values(surname=customer.surname, contact_info=customer.contact_info))
        session.commit()

def delete_soft_customer(customer):
    with Session(engine) as session:
        session.execute(update(Customer).where(Customer.id == customer.id).values(surname="", contact_info=customer.contact_info))
        session.commit()


if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
