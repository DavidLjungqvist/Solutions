"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Anvend det, du har lært i dette kapitel om databaser, på en denne opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select
from sqlalchemy import Float

Database = 'sqlite:///S2311_my_second_sql_database.db'
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer({self.id=} {self.name=} {self.address=} {self.age=}\n)"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Float)
    brand = Column(String)

    def __repr__(self):
        return f"Product({self.id=} {self.product_number=} {self.price=} {self.brand=})\n"


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Customer(name="james", address="pinneapple road", age=25))
        new_items.append(Customer(name="steven", address="watermelon street", age=61))
        new_items.append(Customer(name="bob", address="peach avenue", age=43))
        new_items.append(Customer(name="frank", address="orange square", age=89))
        new_items.append(Product(product_number=12, price=12.99, brand="angelico"))
        new_items.append(Product(product_number=34, price=15.95, brand="stormlife"))
        new_items.append(Product(product_number=56, price=9.45, brand="thundernite"))
        new_items.append(Product(product_number=78, price=19.19, brand="purbleworth"))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)


# create_test_data()

print(select_all(Customer))
print(select_all(Product))

print(get_record(Customer, 1))