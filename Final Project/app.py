from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///canyonings.db")

@app.route("/")
def index():
    cities = db.execute("SELECT * FROM city")
    return render_template("index.html", cities=cities)

@app.route("/choose_river", methods=["POST"])
def choose_river():
    city_id = request.form.get("city_id")
    city_name = db.execute("SELECT name FROM city WHERE id = :city_id", city_id=city_id)[0]["name"]
    rivers = db.execute("SELECT * FROM river WHERE city_id = :city_id", city_id=city_id)
    return render_template("choose_river.html", city_name=city_name, rivers=rivers, city_id=city_id)

@app.route("/view_river", methods=["POST"])
def view_river():
    river_id = request.form.get("river_id")
    river_info = db.execute("SELECT * FROM river WHERE id = :river_id", river_id=river_id)[0]
    city_name = db.execute("SELECT name FROM city WHERE id = :city_id", city_id=river_info["city_id"])[0]["name"]
    return render_template("view_river.html", river_info=river_info, city_name=city_name)

if __name__ == "__main__":
    app.run(debug=True)
