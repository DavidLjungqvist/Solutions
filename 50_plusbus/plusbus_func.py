from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql

def capacity_available(travel_id, new_booking):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.travel_id == travel_id))
        reserved_seats = 0
        for record in records
            reserved_seats += pbsql.get_record(pbd.Customer, record.customer_id).weight
        return booking.