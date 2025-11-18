from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

from plusbus_data import Customer, Travel, Base

Database = 'sqlite:///plusbus.db'


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Customer(date="01/10/2020", capacity="5", route="Viborg - Aarhus"))
        new_items.append(Customer(date="01/10/2020", capacity="5", route="Viborg - Aarhus"))
        new_items.append(Customer(date="01/10/2020", capacity="5", route="Viborg - Aarhus"))
        session.add_all(new_items)
        session.commit()

def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam)) # list of objects??
        result = []
        for record in records:
            result.append(record)
    return result

def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record

def create_record(record):
    with Session(engine) as session:
        if not record.id:
            record.id = None  # sqlalchemy decides ID
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

def update_travel(travel):
    with Session(engine) as session:
        session.execute(update(Travel).where(Travel.id == travel.id).values(route=travel.route, date=travel.date, capacity=travel.capacity))
        session.commit()

def delete_soft_travel(travel):
    with Session(engine) as session:
        session.execute(update(Travel).where(Travel.id == travel.id).values(route="", date=travel.date, capacity=travel.capacity))


if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    # create_test_data()
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
