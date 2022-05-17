from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from app.database import get_db, engine
from app.models import Truck, Car

session = Session(bind=engine)

app = FastAPI()


@app.post("/buytruck")
def Bu_car(data: Car, db: Session = Depends(get_db)):
    truck_data = Truck(
        car_number=data.car_number,
        car_model=data.car_model,
        car_color=data.car_color
    )
    print("database", db)
    db.add(truck_data)
    db.commit()
    db.refresh(truck_data)
    return truck_data


@app.get("/")
def get():
    result = session.exec(select(Truck)).all()
    return result
