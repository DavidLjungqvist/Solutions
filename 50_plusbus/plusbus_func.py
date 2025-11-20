from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql

def booked_seats(booking):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.travel_id == booking.travel_id))
        reserved_seats = 0
        for record in records:
            reserved_seats += pbsql.get_record(pbd.Travel, record.travel_id).reserved_seats
    return reserved_seats

def capacity_available(booking, new_booked_seats):
    booked = booked_seats(booking)
    return travel.capacity > booked + new_booked_seats