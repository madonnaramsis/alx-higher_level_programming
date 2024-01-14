#!/usr/bin/python3
"""
    deletes States that contains 'a' letter.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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
    newState = State(name="California")
    newCity = City(name="San Francisco", state=newState)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
    engine.dispose()
