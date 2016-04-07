from fooflask import app, db, Personne


@app.route("/")
def hello():
    result = db.session.execute("select * from personne")
    return str(list(result))


@app.route("/add/<name>")
def add(name):
    personne = Personne(name=name)
    db.session.add(personne)
    db.session.commit()
    return ''
