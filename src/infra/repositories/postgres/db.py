import contextlib
import logging
from functools import wraps

from flask import Flask
from greenlet import getcurrent
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

logger = logging.getLogger(__name__)

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=naming_convention)
Base = declarative_base(metadata=metadata)
session_factory = sessionmaker(autocommit=False, autoflush=True, bind=None)
session = scoped_session(session_factory, scopefunc=getcurrent)

def init_app(app: Flask):
    engine = create_engine(app.config["SQL_URL"])
    session.configure(bind=engine)

    # https://github.com/pallets-eco/flask-sqlalchemy/blob/main/src/flask_sqlalchemy/extension.py#L406
    app.teardown_appcontext(_teardown_session)

def transactional(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
    return wrapper

def _teardown_session(resp_or_exc):
    with contextlib.suppress(Exception):
        session.remove()
    return resp_or_exc
