from sqlalchemy.orm import Session
from sqlalchemy import select
from tkinter import messagebox

import plusbus_data as pbd
import plusbus_sql as pbsql

# def booked_seats(booking_travel_id):
#     with Session(pbsql.engine) as session:
#         records = session.scalars(select(pbd.Booking).where(pbd.Booking.travel_id == int(booking_travel_id)))
#         reserved_seats = 0
#         for record in records:
#             reserved_seats += record.reserved_seats
#     return reserved_seats

def booked_seats(booking_travel_id, exlude_id=None):
    with Session(pbsql.engine) as session:
        stmt = select(pbd.Booking).where(pbd.Booking.travel_id == int(booking_travel_id))
        if exlude_id is not None:
            stmt = stmt.where(pbd.Booking.id != exlude_id)
        records = session.scalars(stmt)
        reserved_seats = 0
        for record in records:
            reserved_seats += record.reserved_seats
    return reserved_seats

def capacity_available(booking, travel):
    booked = booked_seats(booking.travel_id, booking.id)
    return travel.capacity >= booked + int(booking.reserved_seats)

def integer_check(entry):
    try:
        int(entry)
    except ValueError:
        messagebox.showerror("", "Entries could not be converted to integer")

# def capacity_available_update(booking, travel):
#     booked = booked_seats(booking.travel_id)
#     booked_final = booked - booking.reserved_seats
#     return travel.capacity >= booked + int(booking.reserved_seats)
