from typing import Optional

from sqlmodel import SQLModel, Field


class Car(SQLModel):
    car_number: str
    car_model: str
    car_color: str


class TuckCreate(Car):
    truck_price: float


class Truck(Car, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
