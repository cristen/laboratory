import pytest
import factory
from pytest_factoryboy import register
from factory.alchemy import SQLAlchemyModelFactory
from fooflask import app as fooapp, configure_app, configure_db, Personne
from sqlalchemy.orm import sessionmaker






@pytest.fixture(scope='session')
def app():
    app = configure_app()
    return fooapp

@pytest.yield_fixture(scope='function', autouse=True)
def db_session(app):
    db = configure_db()
    Session = sessionmaker(bind=db)
    session = Session()
    session.begin_nested()
    yield session
    session.rollback()
    session.close()


@register
class PersonneFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Personne
        sqlalchemy_session = db_session

    name = factory.Sequence(lambda n: 'personne_{}'.format(n))
