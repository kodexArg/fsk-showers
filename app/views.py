from app import app



@app.route("/")
def index():
    return "Hellow World!"


@app.route("/about")
def about():
    return "About!"
