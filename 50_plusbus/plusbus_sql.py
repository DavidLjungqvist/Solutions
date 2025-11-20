from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from plusbus_data import Customer, Travel, Booking, Base

Database = 'sqlite:///plusbus.db'


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Booking(customer_id=3, travel_id=4, reserved_seats=2))
        new_items.append(Customer(surname="Johnson", contact_info="johson@gmail.com"))
        new_items.append(Customer(surname="Carlson", contact_info="cson@gmail.com"))
        new_items.append(Customer(surname="Jefferson", contact_info="jefson@gmail.com"))
        new_items.append(Travel(route="København - Roskilde", date=date(2020, 1 ,10), capacity=20))
        new_items.append(Travel(route="København - Helsingør", date=date(2020, 2, 10), capacity=20))
        new_items.append(Travel(route="København - Slagelse", date=date(2020, 3, 10), capacity=20))
        new_items.append(Travel(route="København - Køge", date=date(2020, 4, 10), capacity=20))
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

def update_booking(booking):
    with Session(engine) as session:
        session.execute(update(Booking).where(Booking.id == booking.id).values(customer_id=booking.customer_id, travel_id=booking.travel_id, reserved_seats=booking.reserved_seats))
        session.commit()

def delete_hard_booking(booking):
    with Session(engine) as session:
        session.execute(delete(Booking).where(Booking.id == booking.id))
        session.commit()

if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    # create_test_data()
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
