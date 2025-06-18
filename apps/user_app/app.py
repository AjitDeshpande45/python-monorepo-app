from flask import Flask, render_template, request, redirect, url_for
from user_repo import create_user_table, add_user, get_all_users

app = Flask(__name__)
create_user_table()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_user", methods=["POST"])
def add_user_route():
    name = request.form["name"]
    email = request.form["email"]
    try:
        add_user(name, email)
        return redirect(url_for("user_list"))
    except Exception as e:
        return f"Error: {e}"


@app.route("/users")
def user_list():
    users = get_all_users()
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
