from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

def configure_db():
    db = SQLAlchemy(app)
    return db


def configure_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql+psycopg2://localhost/fooflask')
    return app

Base = declarative_base()


class Personne(Base):
    __tablename__ = 'personne'
    name = Column(String, primary_key=True)


app = configure_app()
db = configure_db()



@app.before_request
def before_request():
    db.session.execute("drop table if exists personne")
    db.session.execute("create table personne (name varchar)")
    db.session.execute("insert into personne (name) values ('moi')")
    db.session.commit()


from laboratory.routes import *
if __name__ == "__main__":
    app.run(debug=True)

