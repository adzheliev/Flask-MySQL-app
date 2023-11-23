from flask import Flask, render_template
import pymysql


app = Flask(__name__)

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "12081984zZ"
        db = "test_aws"
        self.con = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.con.cursor()

    def list_users(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        return result


@app.route('/')
def index():
    def db_query():
        db = Database()
        users = db.list_users()
        return users

    res = db_query()

    return render_template("index.html", result=res)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
