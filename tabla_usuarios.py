"""Tabla usuarios."""

# Flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def get_users():

    # Data source
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template(
        "tabla_usuarios.html",
        usuarios=users
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)