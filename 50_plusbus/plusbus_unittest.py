import unittest
from datetime import date
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine
import plusbus_gui as pbg
import plusbus_data as pbd
import plusbus_sql as pbsql

class TestStringMethods(unittest.TestCase):  # basic example from https://docs.python.org/3/library/unittest.html

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestEmptyEntries(unittest.TestCase):

    def test_empty_container_entries(self):
        # arrange
        Database = 'sqlite:///plusbus.db'  # first part: database type, second part: file path
        Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.
        engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            new_items = []
            new_items.append(pbd.Customer(surname="Johnson", contact_info="Johnson@email.com"))  # add new container to database
            new_items.append(pbd.Travel(route="København - Slagelse", date=date(2020, 10, 20), capacity=5))  # add new aircraft to database
            session.add_all(new_items)
            session.commit()
        record = (None, pbsql.max_id(pbd.Customer), pbsql.max_id(pbd.Travel), 6)  # create a tuple using the newly added container and aircraft (because they have been newly added, they each have the highest id in their table)
        # act
        pbg.create_booking(pbg.tree_booking, record)
        # assert
        self.assertEqual(pbg.INTERNAL_ERROR_CODE, 1)  # container weighs more than the aircraft's total capacity


if __name__ == '__main__':
    unittest.main()
