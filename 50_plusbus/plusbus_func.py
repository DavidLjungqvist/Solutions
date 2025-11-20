from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql

def booked_seats(booking_travel_id):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.travel_id == int(booking_travel_id)))
        reserved_seats = 0
        for record in records:
            reserved_seats += record.reserved_seats
    return reserved_seats

def capacity_available(booking, travel):
    booked = booked_seats(booking.travel_id)
    return travel.capacity >= booked + int(booking.reserved_seats)
