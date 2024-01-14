#!/usr/bin/python3
"""
    prints all City objects in the given db.
"""
import sys
from sqlalchemy import create_engine, collate
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = (
        session.query(City, State)
               .filter(City.state_id == State.id)
               .order_by(City.id)
               .all()
    )
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
    engine.dispose()
