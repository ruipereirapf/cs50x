import os, datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    transactions_db = db.execute(
        "SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id= ? GROUP BY symbol",
        user_id,
    )
    cash_db = db.execute("SELECT cash FROM users WHERE id= ?", user_id)
    cash = cash_db[0]["cash"]

    return render_template("index.html", database=transactions_db, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
            return apology("Symbol can not be empty.")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol not valid.")

        if shares < 0:
            return apology("Invalid Share Value.")

        transaction_value = shares * stock["price"]

        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id= ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        if user_cash < transaction_value:
            return apology("Not Enough Money")

        update_cash = user_cash - transaction_value

        db.execute("UPDATE users SET cash = ? WHERE id= ?", update_cash, user_id)

        date = datetime.datetime.now()

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
            user_id,
            stock["symbol"],
            shares,
            stock["price"],
            date,
        )

        flash("Stock Bought!")
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute("SELECT * FROM transactions WHERE user_id= ?", user_id)
    return render_template("history.html", transactions=transactions_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Symbol can not be empty.")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol not validm")
        return render_template(
            "quoted.html",
            name=stock["name"],
            price=stock["price"],
            symbol=stock["symbol"],
        )


@app.route("/register", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Username can not be empty.")
        if not password:
            return apology("Password can not be empty.")
        if not confirmation:
            return apology("Password Confirmation can not be empty.")
        if password != confirmation:
            return apology("Password and Password Confirmation do not match.")

        # Check if password contains both letters and numbers
        if not any(char.isalpha() for char in password) or not any(
            char.isdigit() for char in password
        ):
            return apology("Password must contain both letters and numbers.")

        hash = generate_password_hash(password)

        try:
            new_user = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
            )
        except:
            return apology("Username already in use.")

        session["user_id"] = new_user

        return redirect("/")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """Change Password"""

    if request.method == "GET":
        return render_template("changepassword.html")
    elif request.method == "POST":
        # Get user's input from the form
        old_password = request.form.get("password")
        new_password = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")

        # Ensure old password is provided
        if not old_password:
            return apology("Old Password can not be empty.")

        # Query the database for the user's current password hash
        user_id = session["user_id"]
        user_data = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        # Verify the old password
        if not check_password_hash(user_data[0]["hash"], old_password):
            return apology("Incorrect old password.")

        # Ensure new password and confirmation match
        if new_password != confirmation:
            return apology("New Password and Confirmation do not match.")

        # Check if new password contains both letters and numbers
        if not any(char.isalpha() for char in new_password) or not any(
            char.isdigit() for char in new_password
        ):
            return apology("New Password must contain both letters and numbers.")

        # Generate hash for the new password
        new_password_hash = generate_password_hash(new_password)

        # Update the user's password in the database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_password_hash, user_id)

        flash("Password changed successfully!")
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols_user = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id,
        )
        return render_template(
            "sell.html", symbols=[row["symbol"] for row in symbols_user]
        )
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
            return apology("Symbol can not be empty.")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol not valid.")

        if shares < 0:
            return apology("Invalid Share Value.")

        transaction_value = shares * stock["price"]

        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id= ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        user_shares = db.execute(
            "SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",
            user_id,
            symbol,
        )
        user_shares_real = user_shares[0]["shares"]

        if shares > user_shares_real:
            return apology("Not enought shares.")

        update_cash = user_cash + transaction_value

        db.execute("UPDATE users SET cash = ? WHERE id= ?", update_cash, user_id)

        date = datetime.datetime.now()

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
            user_id,
            stock["symbol"],
            (-1) * shares,
            stock["price"],
            date,
        )

        flash("Stock Sold!")
        return redirect("/")
