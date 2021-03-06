#!/usr/bin/python3
""" Script that lists all State objects from a database """

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    o = s.query(State).order_by(State.id).first()
    if o:
        print("{}: {}".format(o.id, o.name))
    else:
        print("Nothing")
    s.close()
